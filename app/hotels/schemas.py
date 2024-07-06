from typing import Optional

from fastapi import Query
from pydantic import BaseModel, EmailStr
from datetime import datetime


class SgetAllHotels(BaseModel):
    location: str


class SGetHotel(BaseModel):
    date_from: datetime
    date_to: datetime
    location: str


class HotelSearchArgs():
    def __init__(
            self,
            location: str,
            date_from: datetime,
            date_to: datetime,
            stars: Optional[int] = Query(ge=1, le=5),
            has_spa: Optional[bool] = None
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa
