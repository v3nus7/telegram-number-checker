"""
Telegram Number Checker Module

A Python module for checking Telegram phone numbers using the IRBots API.
Provides 100% precision phone number analysis for Telegram accounts.

Usage:
    from telegram_checker import TelegramChecker
    
    checker = TelegramChecker(api_key="your_api_key_here")
    result = checker.check_number("+1234567890")
    print(result)
"""

import urllib.request
import urllib.parse
import urllib.error
import json
from typing import Optional, Dict, Any


class TelegramCheckerError(Exception):
    """Base exception for Telegram Checker errors."""
    pass


class APIKeyError(TelegramCheckerError):
    """Raised when API key is not set or invalid."""
    pass


class APIRequestError(TelegramCheckerError):
    """Raised when API request fails."""
    pass


class TelegramChecker:
    """
    A client for checking Telegram phone numbers using the IRBots API.
    
    Attributes:
        api_key (str): The API key for authentication.
        base_url (str): The base URL of the API endpoint.
    
    Example:
        >>> checker = TelegramChecker(api_key="your_api_key")
        >>> result = checker.check_number("+1234567890")
        >>> print(result)
    """
    
    BASE_URL = "https://irbots.com/TG-Number-Analyzer/api.php"
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the TelegramChecker instance.
        
        Args:
            api_key: Your API key for the IRBots service.
                     Can be set later using set_api_key() method.
        """
        self._api_key: Optional[str] = api_key
    
    @property
    def api_key(self) -> Optional[str]:
        """Get the current API key."""
        return self._api_key
    
    def set_api_key(self, api_key: str) -> None:
        """
        Set or update the API key.
        
        Args:
            api_key: Your API key for the IRBots service.
        
        Raises:
            APIKeyError: If the api_key is empty or None.
        """
        if not api_key or not api_key.strip():
            raise APIKeyError("API key cannot be empty")
        self._api_key = api_key.strip()
    
    def check_number(self, phone_number: str) -> Dict[str, Any]:
        """
        Check a phone number on Telegram.
        
        Args:
            phone_number: The phone number to check. Should include country code
                         (e.g., "+1234567890" or "1234567890").
        
        Returns:
            A dictionary containing the API response with phone number details.
        
        Raises:
            APIKeyError: If the API key is not set.
            APIRequestError: If the API request fails.
            ValueError: If the phone number is invalid.
        
        Example:
            >>> checker = TelegramChecker(api_key="your_key")
            >>> result = checker.check_number("+1234567890")
            >>> if result.get("success"):
            ...     print(f"Status: {result.get('status')}")
        """
        if not self._api_key:
            raise APIKeyError("API key is not set. Use set_api_key() or pass it to the constructor.")
        
        # Validate phone number
        cleaned_number = self._clean_phone_number(phone_number)
        if not cleaned_number:
            raise ValueError("Invalid phone number format")
        
        # Build request
        params = {
            "api_key": self._api_key,
            "phone": cleaned_number
        }
        
        url = f"{self.BASE_URL}?{urllib.parse.urlencode(params)}"
        
        try:
            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "TelegramChecker-Python/1.0",
                    "Accept": "application/json"
                }
            )
            
            with urllib.request.urlopen(request, timeout=30) as response:
                data = response.read().decode("utf-8")
                return json.loads(data)
                
        except urllib.error.HTTPError as e:
            raise APIRequestError(f"HTTP Error {e.code}: {e.reason}")
        except urllib.error.URLError as e:
            raise APIRequestError(f"URL Error: {e.reason}")
        except json.JSONDecodeError as e:
            raise APIRequestError(f"Failed to parse API response: {e}")
        except TimeoutError:
            raise APIRequestError("Request timed out")
    
    def _clean_phone_number(self, phone_number: str) -> str:
        """
        Clean and validate a phone number.
        
        Args:
            phone_number: The raw phone number string.
        
        Returns:
            Cleaned phone number containing only digits and optional leading +.
        """
        if not phone_number:
            return ""
        
        # Remove spaces, dashes, parentheses
        cleaned = phone_number.strip()
        
        # Keep + at the beginning if present
        has_plus = cleaned.startswith("+")
        
        # Keep only digits
        cleaned = "".join(c for c in cleaned if c.isdigit())
        
        if not cleaned:
            return ""
        
        # Add + back if it was there
        if has_plus:
            cleaned = "+" + cleaned
        
        return cleaned
    
    def is_configured(self) -> bool:
        """
        Check if the API key is configured.
        
        Returns:
            True if API key is set, False otherwise.
        """
        return bool(self._api_key)
    
    def __repr__(self) -> str:
        """Return string representation of the checker instance."""
        configured = "configured" if self.is_configured() else "not configured"
        return f"TelegramChecker({configured})"


# Convenience function for quick checks
def check_telegram_number(phone_number: str, api_key: str) -> Dict[str, Any]:
    """
    Convenience function to check a Telegram number without creating an instance.
    
    Args:
        phone_number: The phone number to check.
        api_key: Your API key for the IRBots service.
    
    Returns:
        A dictionary containing the API response.
    
    Example:
        >>> result = check_telegram_number("+1234567890", "your_api_key")
        >>> print(result)
    """
    checker = TelegramChecker(api_key=api_key)
    return checker.check_number(phone_number)
