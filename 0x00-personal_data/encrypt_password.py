#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password with bcrypt and return the hashed password"""
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the generated salt
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
