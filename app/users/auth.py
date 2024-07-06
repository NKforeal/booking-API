import jwt
from app.config import settings
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pydantic import EmailStr

from app.exceptions import UserNotFoundException, IncorrectPassword
from app.users.dao import UsersDAO

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode,
                             settings.SECRET_KEY,
                             settings.CIPHER)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str) -> list['Users']:
    user = await UsersDAO.find_one_or_none(email=email)

    if not user:
        raise UserNotFoundException
    if not verify_password(password, user['Users'].hashed_password):
        raise IncorrectPassword

    return user

