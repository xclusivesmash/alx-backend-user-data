#!/usr/bin/env python3
"""
module: auth
description: authorization module.
"""
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ encoded the password using bcrypt.
    Args:
        password (str): input password.
    Returns:
        encoded password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ generates a unique id.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ registers a new user
        Args:
            email (str): user email.
            password (str): user password.
        Returns:
            User object.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        else:
            # user already exists.
            raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ validates login.
        Args:
            email (str): user email.
            password (str): user password.
        Returns:
            True if user is authenticated. Else False.
        """
        try:
            # find the user with the given email
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        # check validity of password
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """ Finds the user corresponding to the email,
        generate a new UUID and store it in the database as the user’s
        session_id, then return the session ID.
        Args:
            email (str): user email.
        Returns:
            session ID.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            user.session_id = _generate_uuid()
        return user.session_id
