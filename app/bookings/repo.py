from datetime import datetime

from sqlalchemy import select, and_, or_, func, insert

from app.DAO.base import BaseDAO
from app.bookings.models import Booking
from app.database import async_session_maker
from app.hotels.rooms.model import Rooms


class BookingDAO(BaseDAO):
    model = Booking

    @classmethod
    async def add_booking(cls,
                          user_id: int,
                          room_id: int,
                          date_from: datetime,
                          date_to: datetime,
                          ):
        booked_rooms = select(Booking).where(
            and_(
                Booking.room_id == room_id,
                or_(
                    and_(
                        Booking.date_from >= date_to,
                        Booking.date_from <= date_from
                    ),
                    and_(
                        Booking.date_from <= date_from,
                        Booking.date_to > date_from
                    )

                )
            )
        ).cte("booked_rooms")

        get_rooms_left = select(
            (Rooms.quantity - func.count(booked_rooms.c.room_id)).label("rooms_left")
        ).select_from(Rooms).join(
            booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
        ).where(Rooms.id == room_id).group_by(
            Rooms.quantity, booked_rooms.c.room_id
        )

        async with async_session_maker() as session:
            rooms_left = await session.execute(get_rooms_left)

            rooms_left: int = rooms_left.scalar()

            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()

                add_booking = insert(Booking).values(
                    room_id=room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price,
                ).returning(Booking)

                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.unique().scalars()
            else:
                return None
