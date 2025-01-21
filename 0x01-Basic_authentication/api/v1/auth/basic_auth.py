#!/usr/bin/env python3
"""
module: basic_auth
description: handles authorization.
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ @description
    BasicAuth class definition.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header
        Args:
            authorization_header (str): content of the Authorization header.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        token = authorization_header.split(' ')[-1]
        return token

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ decodes the base64_authorization_header string using base64
        Args:
            base64_authorization_header (str): not decoded string.
        Returns:
            decoded value of base64_authorization_header.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            # 1. encode
            encoded = base64_authorization_header.encode('utf-8')
            # 2. decode using base64
            b64 = base64.b64decode(encoded)
            # 3. decode
            decoded = b64.decode('utf-8')
            return decoded
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ Extracts user credentials.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email, paswrd = decoded_base64_authorization_header.split(':')
        return (email, paswrd)
