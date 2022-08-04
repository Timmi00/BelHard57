from pydantic import BaseModel, Field
from datetime import datetime


class ArticleCommentSchema(BaseModel):
    user_id: int = Field()
    article_id: int = Field()
    date_created: datetime = Field(default=datetime.utcnow())


class ArticleCommentInDBSchema(ArticleCommentSchema):
    id: int = Field(ge=1)
