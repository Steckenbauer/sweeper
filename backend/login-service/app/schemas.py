import re
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def normalize_email(value: str) -> str:
    email = value.strip().lower()
    if len(email) > 320 or not EMAIL_PATTERN.fullmatch(email):
        raise ValueError("A valid email address is required")
    return email


class PasswordRegistration(BaseModel):
    email: str
    password: str = Field(min_length=12, max_length=128)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        return normalize_email(value)


class PasswordLogin(BaseModel):
    email: str
    password: str = Field(min_length=1, max_length=128)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        return normalize_email(value)


class OneTimeCodeExchange(BaseModel):
    code: str = Field(min_length=32, max_length=256)


class PasskeyRegistrationVerification(BaseModel):
    flow_id: UUID
    credential: dict[str, Any]
    display_name: str | None = Field(default=None, max_length=100)


class PasskeyAuthenticationVerification(BaseModel):
    flow_id: UUID
    credential: dict[str, Any]


class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class UserResponse(BaseModel):
    id: str
    email: str | None
