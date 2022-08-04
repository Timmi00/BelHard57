from typing import Optional, List
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from BelHard57.models import create_session, Article
from BelHard57.schemas import ArticleSchema, ArticleInDBSchema


class CRUDArticle:

    @staticmethod
    @create_session
    def add(article: ArticleSchema, session: Session = None) -> Optional[ArticleInDBSchema]:
        article = Article(**article.dict())
        session.add(article)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(article)
            return ArticleInDBSchema(**article.__dict__)

    @staticmethod
    @create_session
    def get(article_id: int, session: Session = None) -> Optional[ArticleInDBSchema]:
        article = session.execute(
            select(Article)
            .where(Article.id == article_id)
        )
        article = article.first()
        if article:
            return ArticleInDBSchema(**article[0].__dict__)

    @staticmethod
    @create_session
    def get_all(parent_id: int = None, session: Session = None) -> List[ArticleInDBSchema]:
        if parent_id:
            articles = session.execute(
                select(Article)
                .where(Article.parent_id == parent_id)
                .order_by(Article.id)
            )
        else:
            articles = session.execute(
                select(Article)
                .order_by(Article.id)
            )
        return [ArticleInDBSchema(**article[0].__dict__) for article in articles]

    @staticmethod
    @create_session
    def delete(article_id: int, session: Session = None) -> None:
        session.execute(
            delete(Article)
            .where(Article.id == article_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(
            article: ArticleInDBSchema,
            session: Session = None
    ) -> bool:
        session.execute(
            update(Article)
            .where(Article.id == article.id)
            .values(**article.dict())
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True
