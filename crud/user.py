from typing import Optional, List
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from BelHard57.models import create_session, User
from BelHard57.schemas import UserSchema, UserInDBSchema


class CRUDUser:

    @staticmethod
    @create_session
    def add(user: UserSchema, session: Session = None) -> Optional[UserInDBSchema]:
        user = User(**user.dict())
        session.add(user)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(user)
            return UserInDBSchema(**user.__dict__)

    @staticmethod
    @create_session
    def get(user_id: int, session: Session = None) -> Optional[UserInDBSchema]:
        user = session.execute(
            select(User)
            .where(User.id == user_id)
        )
        user = user.first()
        if user:
            return UserInDBSchema(**user[0].__dict__)

    @staticmethod
    @create_session
    def get_all(parent_id: int = None, session: Session = None) -> List[UserInDBSchema]:
        if parent_id:
            users = session.execute(
                select(User)
                .where(User.parent_id == parent_id)
                .order_by(User.id)
            )
        else:
            users = session.execute(
                select(User)
                .order_by(User.id)
            )
        return [UserInDBSchema(**user[0].__dict__) for user in users]

    @staticmethod
    @create_session
    def delete(user_id: int, session: Session = None) -> None:
        session.execute(
            delete(User)
            .where(User.id == user_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(
            user: UserInDBSchema,
            session: Session = None
    ) -> bool:
        session.execute(
            update(User)
            .where(User.id == user.id)
            .values(**user.dict())
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True
