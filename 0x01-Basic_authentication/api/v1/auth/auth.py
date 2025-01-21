#!/usr/bin/env python3
"""
module: auth
description: handling authorization.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class definition.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ checks for the path against the excluded ones.
        Args:
            path (str): path to be checked.
            excluded_paths (List[str]): excluded paths.
        Returns:
            False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Handles the request method.
        Args:
            request (Flask.request): request object from Flask.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
