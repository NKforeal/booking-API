from pydantic import BaseModel
from datetime import date, datetime


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        from_attributes = True


class SAddBooking(BaseModel):
    user_id: int
    room_id: int
    date_from: datetime
    date_to: datetime
