# Telegram Number Checker

A Python module for checking Telegram phone numbers using the IRBots API with 100% precision.

## Features

- Easy to use Python module
- Simple API key configuration
- Phone number validation and cleaning
- Comprehensive error handling
- Type hints for better IDE support

## Installation

1. Download the `telegram_checker.py` file
2. Place it in your project directory
3. Import and use it in your code

```bash
# Clone the repository
git clone https://github.com/v3nus7/telegram-number-checker.git

# Or simply download telegram_checker.py and place it in your project
```

## Getting an API Key

To use this module, you need an API key from [IRBots TG Number Analyzer](https://irbots.com/TG-Number-Analyzer/).

## Quick Start

```python
from telegram_checker import TelegramChecker

# Create a checker instance with your API key
checker = TelegramChecker(api_key="your_api_key_here")

# Check a phone number
result = checker.check_number("+1234567890")
print(result)
```

## Usage Examples

### Method 1: Initialize with API Key

```python
from telegram_checker import TelegramChecker

# Create instance with API key
checker = TelegramChecker(api_key="your_api_key_here")

# Check a number
result = checker.check_number("+1234567890")
```

### Method 2: Set API Key Later

```python
from telegram_checker import TelegramChecker

# Create instance without API key
checker = TelegramChecker()

# Set API key later
checker.set_api_key("your_api_key_here")

# Check a number
result = checker.check_number("+1234567890")
```

### Method 3: Using Convenience Function

```python
from telegram_checker import check_telegram_number

# Quick one-liner check
result = check_telegram_number("+1234567890", "your_api_key_here")
```

### Error Handling

```python
from telegram_checker import TelegramChecker, TelegramCheckerError, APIKeyError, APIRequestError

checker = TelegramChecker(api_key="your_api_key_here")

try:
    result = checker.check_number("+1234567890")
    
    if result.get("success"):
        print("Number found on Telegram!")
        print(f"Details: {result}")
    else:
        print("Number not found or error occurred")
        print(f"Message: {result.get('message')}")
        
except APIKeyError as e:
    print(f"API Key Error: {e}")
except APIRequestError as e:
    print(f"API Request Error: {e}")
except ValueError as e:
    print(f"Invalid phone number: {e}")
```

## API Reference

### TelegramChecker Class

#### Constructor

```python
TelegramChecker(api_key: Optional[str] = None)
```

- `api_key`: Your API key for the IRBots service (optional, can be set later)

#### Methods

| Method | Description |
|--------|-------------|
| `set_api_key(api_key: str)` | Set or update the API key |
| `check_number(phone_number: str)` | Check a phone number on Telegram |
| `is_configured()` | Check if API key is configured |

### Exceptions

| Exception | Description |
|-----------|-------------|
| `TelegramCheckerError` | Base exception for all checker errors |
| `APIKeyError` | Raised when API key is not set or invalid |
| `APIRequestError` | Raised when API request fails |

## Phone Number Format

The module accepts phone numbers in various formats:
- With country code: `+1234567890`
- Without plus: `1234567890`
- With spaces or dashes: `+1 234-567-890`

The module automatically cleans and validates the phone number before sending to the API.

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
