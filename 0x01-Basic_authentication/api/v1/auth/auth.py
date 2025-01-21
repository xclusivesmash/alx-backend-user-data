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
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        # fix slash '/' tolerance
        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False
        return True

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
