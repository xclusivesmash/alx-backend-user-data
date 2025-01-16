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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ checks password validity
    Args:
        hash_password (bytes): a hashed password from bcrypt.
        password (str): input password as a string
    Returns:
        boolean value indicating if the 2 args match or not.
    """
    check = False
    password_encoded = password.encode()
    if bcrypt.checkpw(password_encoded, hashed_password):
        check = True
    return check
