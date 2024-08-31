import bcrypt

def hash_password(password: str) -> bytes:
    """Hash a password with bcrypt and return the hashed password as a byte string."""
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the generated salt
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
