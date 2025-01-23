#!/usr/bin/env python3
"""
module: auth
description: authorization module.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ encoded the password using bcrypt.
    Args:
        password (str): input password.
    Returns:
        encoded password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
