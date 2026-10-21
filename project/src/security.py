from datetime import datetime, timedelta
from typing import Optional
from pwdlib import PasswordHash
import jwt
from os import getenv
from dotenv import load_dotenv

# Password context for hashing
pwd_context = PasswordHash.recommended()
load_dotenv()
SECRET_KEY = getenv("SECRET_KEY")


class Security:
    """Security utilities."""

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash."""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        """Get the hash of a password."""
        return pwd_context.hash(password)

    @staticmethod
    def create_access_token(
        data: dict, expires_delta: Optional[timedelta] = None
    ) -> str:
        """Create an access token."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta  # FIXME: utcnow
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
        return encoded_jwt

    @staticmethod
    def decode_token(token: str) -> dict:
        """Decode a JWT token."""
        # try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
        # except jw as e:
        #     raise ValueError(f"Invalid token: {str(e)}")
