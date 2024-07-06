from typing import List

from fastapi import APIRouter, Depends, Request

from app.exceptions import RoomCannotBeBookedException
from app.users.dependencies import get_current_user
from app.users.models import Users

from app.bookings.repo import BookingDAO
from app.bookings.schemas import SBooking, SAddBooking

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования номера']
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post('/add')
async def add_booking(req: SAddBooking,
                      user: Users = Depends(get_current_user)):
    booking = await BookingDAO.add_booking(user_id=user.id,
                                           room_id=req.room_id,
                                           date_to=req.date_to,
                                           date_from=req.date_from,
                                           )

    if not booking:
        raise RoomCannotBeBookedException

    return booking.unique().all()


@router.get('/get_info')
async def get_bookings(request: Request) -> list[str]:
    return dir(request)


@router.get('/bookings/{booking_id}')
def get_bookings(booking_id):
    pass
