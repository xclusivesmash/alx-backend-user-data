#!/usr/bin/env python3
"""
module: session_auth
description: implements the session authorization.
"""
from .auth import Auth
import uuid


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
