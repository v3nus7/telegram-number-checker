"""
Example usage of the Telegram Number Checker module.

This script demonstrates how to use the TelegramChecker class
to check phone numbers on Telegram.
"""

from telegram_checker import TelegramChecker, check_telegram_number, TelegramCheckerError


def main():
    # Method 1: Create an instance with API key in constructor
    print("=== Method 1: Constructor Initialization ===")
    checker = TelegramChecker(api_key="your_api_key_here")
    
    # Check if configured
    print(f"Checker status: {checker}")
    print(f"Is configured: {checker.is_configured()}")
    
    # Method 2: Create instance first, then set API key
    print("\n=== Method 2: Set API Key Later ===")
    checker2 = TelegramChecker()
    print(f"Before setting key: {checker2}")
    
    checker2.set_api_key("your_api_key_here")
    print(f"After setting key: {checker2}")
    
    # Method 3: Check number using the instance
    print("\n=== Checking a Phone Number ===")
    try:
        # Replace with a real phone number for testing
        result = checker.check_number("+1234567890")
        print(f"Result: {result}")
        
        # Handle the response
        if result.get("success"):
            print("✓ Number check successful!")
            print(f"  Status: {result.get('status')}")
            print(f"  Details: {result.get('data')}")
        else:
            print("✗ Number check failed")
            print(f"  Error: {result.get('message')}")
            
    except TelegramCheckerError as e:
        print(f"Error: {e}")
    
    # Method 4: Using convenience function
    print("\n=== Method 4: Convenience Function ===")
    try:
        result = check_telegram_number("+1234567890", "your_api_key_here")
        print(f"Result: {result}")
    except TelegramCheckerError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
