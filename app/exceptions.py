from typing import Optional
from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self, detail: Optional[str] = None):
        super().__init__(status_code=self.status_code, detail=detail or self.detail)


class UsersExceptions(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self, detail: Optional[str] = None):
        super().__init__(status_code=self.status_code, detail=detail or self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class RoomCannotBeBookedException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Не осталось свободных номеров."


class UserNotFoundException(UsersExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Пользователь не найден"


class IncorrectPassword(UsersExceptions):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Неверный пароль"
