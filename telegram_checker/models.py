from typing import Dict

class CheckResult:
    """Represents the result of checking Telegram numbers."""

    def __init__(self, data: Dict[str, str], time_taken: float, errors: int, status: str):
        self.data = data
        self.time_taken = f"{time_taken} seconds"
        self.errors = errors
        self.status = status

    def __repr__(self):
        return f"<CheckResult status={self.status} errors={self.errors} time_taken={self.time_taken} data={self.data}>"
