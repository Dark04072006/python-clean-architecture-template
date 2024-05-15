class DomainError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class DomainValidationError(DomainError):
    """Exception for domain validation errors"""
