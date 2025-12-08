class TelegramCheckerError(Exception):
    """Base exception for TelegramChecker library."""
    pass


class InvalidAPIKeyError(TelegramCheckerError):
    """Raised when the API key is missing or invalid."""
    pass


class APIRequestError(TelegramCheckerError):
    """Raised when the API request fails."""
    pass


class APIResponseError(TelegramCheckerError):
    """Raised when the API returns an unexpected or malformed response."""
    pass
