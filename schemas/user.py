from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    username: str = Field(max_length=24, unique_items=None)
    hashed_password: str = Field()
    is_blocked: bool = Field(default=False)
    email: EmailStr = Field(unique_items=None)


class UserInDBSchema(UserSchema):
    id: int = Field(ge=1)
