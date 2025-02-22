#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adds user to database.
        Args:
            email (str): user email.
            hashed_password (str): user encoded password.
        Returns:
            user object.
        """
        try:
            user = User(email=email, hashed_password=hashed_password)
            self._session.add(user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            user = None
        return user

    def find_user_by(self, **kwargs) -> User:
        """ gets users from db.
        Args:
            kwargs (dict): key=value pair dictionary.
        Returns:
            user object.
        """
        if not kwargs:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ updates user based on user id.
        Args:
            user_id (int): unique user id.
            kwargs (dict): key=value pairs.
        Returns:
            None.
        """
        user = self.find_user_by(id=user_id)
        if user is None:
            return
        temp = {}
        for k, v in kwargs.items():
            if not hasattr(user, k):
                raise ValueError
            else:
                temp[getattr(User, k)] = v
        # commit to session
        self._session.query(User).filter(User.id == user_id).update(
            temp,
            synchronize_session=False,
        )
        self._session.commit()
        return None
