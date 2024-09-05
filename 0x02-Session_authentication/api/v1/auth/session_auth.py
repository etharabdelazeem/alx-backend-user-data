#!/usr/bin/env python3
"""
The session authentication class
"""
from .auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    session authentication mechanism class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a session id for user
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)
