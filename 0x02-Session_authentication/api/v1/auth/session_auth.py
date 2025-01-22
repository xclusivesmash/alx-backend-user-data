#!/usr/bin/env python3
"""
module: session_auth
description: implements the session authorization.
"""
from .auth import Auth
import uuid
from models.user import User
from flask import request


class SessionAuth(Auth):
    """ @description.
    SessionAuth class definition.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a server session.
        Args:
            user_id (str): Id of a user.
        Returns:
            session ID.
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        sessionID = str(uuid.uuid4())
        self.user_id_by_session_id[sessionID] = user_id
        return sessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns id based on session id.
        Args:
            session_id (str): session id.
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns a user instance based on cookie value.
        Args:
            request: request objetct.
        """
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        user = User.get(user_id)
        return user
