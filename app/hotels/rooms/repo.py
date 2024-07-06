from sqlalchemy import select

from app.DAO.base import BaseDAO
from app.database import async_session_maker
from app.hotels.rooms.model import Rooms


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_all_quantity(cls, quantity: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(quantity=quantity)
            result = session.execute(query)

            return result.mappings().all()
