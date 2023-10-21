"""
Custom exception for invalid operation
"""


class InvalidOperation(Exception):
    def __int__(self, operation: str):
        super().__init__(f"Invalid operation: {operation}")

# EOF
