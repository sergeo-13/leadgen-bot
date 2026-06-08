"""Custom application exceptions."""


class LeadgenException(Exception):
    """Base exception for leadgen application."""

    pass


class DatabaseConnectionError(LeadgenException):
    """Raised when database connection fails."""

    pass


class MinIOConnectionError(LeadgenException):
    """Raised when MinIO connection fails."""

    pass


class HealthCheckError(LeadgenException):
    """Raised when health check fails."""

    pass
