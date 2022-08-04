from pydantic import BaseModel, Field
from datetime import datetime


class ArticleSchema(BaseModel):
    category_id: int = Field()
    title: str = Field(max_length=50)
    body: str = Field(max_length=1024)
    date_created: datetime = Field(default=datetime.utcnow())
    author_id: int = Field()


class ArticleInDBSchema(ArticleSchema):
    id: int = Field(ge=1)

