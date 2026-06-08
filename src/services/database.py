"""Database connection and operations."""

import logging

import asyncpg

from src.config import settings
from src.core.exceptions import DatabaseConnectionError

logger = logging.getLogger(__name__)


async def check_postgres() -> bool:
    """
    Check PostgreSQL connection.

    Returns:
        True if connection is successful, False otherwise.

    Raises:
        DatabaseConnectionError: If connection fails.
    """
    try:
        conn = await asyncpg.connect(
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            database=settings.POSTGRES_DB,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            timeout=5,
        )
        try:
            result = await conn.fetchval("SELECT 1")
            return result == 1
        finally:
            await conn.close()
    except Exception as e:
        logger.error(f"PostgreSQL connection error: {e}")
        raise DatabaseConnectionError(f"Failed to connect to PostgreSQL: {e}")
