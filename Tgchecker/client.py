import httpx
from typing import List, Union

from .exceptions import (
    InvalidAPIKeyError,
    APIRequestError,
    APIResponseError,
)

from .models import CheckResult


BASE_URL = "http://api.irbots.com"


class TgChecker:
    """
    Sync and async client for checking Telegram number statuses.
    """

    def __init__(self, api_key: str, timeout: int = 10):
        """
        Initialize the TelegramChecker client.

        :param api_key: Your API key for irbots.com
        :param timeout: Request timeout in seconds
        """
        if not api_key or not isinstance(api_key, str):
            raise InvalidAPIKeyError("API key is required and must be a string.")

        self.api_key = api_key
        self.timeout = timeout

    # -------------------------------------------------------------------------
    # Utility
    # -------------------------------------------------------------------------

    def _prepare_numbers(self, numbers: Union[str, List[str]]) -> str:
        if numbers == '' or numbers == []:
            raise ValueError("numbers cannot be empty.")
        
        if isinstance(numbers, str) and not numbers.lstrip('+').isdigit():
            raise ValueError("numbers should be a list of strings or a single string with a valid phone number.")
        
        if isinstance(numbers, list) and not all(num.lstrip('+').isdigit() for num in numbers):
            raise ValueError("numbers should be a list of strings or a single string with a valid phone number.")
        
        if isinstance(numbers, str) and len(numbers.lstrip('+')) < 5:
            raise ValueError("Phone number should be at least 5 digits.")
        
        if isinstance(numbers, list):
            for number in numbers:
                if len(number.lstrip('+')) < 5:
                    raise ValueError("Phone number should be at least 5 digits.")
            
        if isinstance(numbers, str):
            return numbers
        
        if isinstance(numbers, list):
            return ",".join(numbers)

        raise ValueError("numbers must be a string or list of strings.")

    # -------------------------------------------------------------------------
    # Sync
    # -------------------------------------------------------------------------

    def check_sync(self, numbers: Union[str, List[str]]) -> CheckResult:
        """
        Check phone numbers synchronously.

        :param numbers: Single number or list of numbers
        :return: CheckResult object
        """
        numbers_str = self._prepare_numbers(numbers)

        params = {
            "key": self.api_key,
            "numbers": numbers_str,
            "target": "checker",
        }

        try:
            response = httpx.get(BASE_URL, params=params, timeout=self.timeout)
        except httpx.RequestError as e:
            raise APIRequestError(f"Sync request failed: {e}") from e

        return self._parse_response(response)

    # -------------------------------------------------------------------------
    # Async
    # -------------------------------------------------------------------------

    async def check_async(self, numbers: Union[str, List[str]]) -> CheckResult:
        """
        Check phone numbers asynchronously.

        :param numbers: Single number or list of numbers
        :return: CheckResult object
        """
        numbers_str = self._prepare_numbers(numbers)

        params = {
            "key": self.api_key,
            "numbers": numbers_str,
            "target": "checker",
        }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.get(BASE_URL, params=params)
            except httpx.RequestError as e:
                raise APIRequestError(f"Async request failed: {e}") from e

        return self._parse_response(response)

    # -------------------------------------------------------------------------
    # Response Parsing
    # -------------------------------------------------------------------------

    def _parse_response(self, response: httpx.Response) -> CheckResult:
        if response.status_code != 200:
            raise APIResponseError(
                f"API returned status {response.status_code}: {response.text}"
            )

        try:
            data = response.json()
        except ValueError:
            raise APIResponseError("Failed to decode JSON response.")

        try:
            return CheckResult(
                data=data.get("data", {}),
                time_taken=data.get("Time taken", 0),
                errors=data.get("errors", 0),
                status=data.get("status", "unknown"),
            )
        except KeyError as e:
            raise APIResponseError(f"Malformed API response, missing key: {e}")
