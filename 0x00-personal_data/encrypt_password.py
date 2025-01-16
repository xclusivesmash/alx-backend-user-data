#!/usr/bin/env python3
"""
module: encrypt_password
description: password encryption using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ encrypts a password using th bcrypt module.
    Args:
        password (str): input password
    Returns:
        a hashed password encrypted using bcrypt.
    """
    passwd_encoded = password.encode()
    hashed = bcrypt.hashpw(passwd_encoded, bcrypt.gensalt())
    return hashed
