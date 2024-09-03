#!/user/bin/env python3
"""
Authentication management class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manages the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication or not
        """
        return False


    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from a request object
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns a User instance from information from a request object
        """
        return None
