"""Pydantic schemas for request/response models."""

from typing import Optional

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response schema."""

    status: str = Field(..., description="Overall system status")
    postgres: bool = Field(..., description="PostgreSQL connection status")
    minio: bool = Field(..., description="MinIO connection status")

    class Config:
        json_schema_extra = {
            "example": {
                "status": "ok",
                "postgres": True,
                "minio": True,
            }
        }


class LeadBase(BaseModel):
    """Base lead schema."""

    name: str = Field(..., description="Lead name")
    email: str = Field(..., description="Lead email")
    company: Optional[str] = Field(None, description="Company name")
    source: str = Field(default="unknown", description="Lead source")


class LeadCreate(LeadBase):
    """Lead creation schema."""

    pass


class Lead(LeadBase):
    """Lead schema with ID."""

    id: int = Field(..., description="Lead ID")
    created_at: str = Field(..., description="Creation timestamp")

    class Config:
        from_attributes = True
