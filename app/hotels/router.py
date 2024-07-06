from fastapi import APIRouter
from datetime import datetime
from app.hotels.repo import HotelsDAO
from app.hotels.schemas import SGetHotel

router = APIRouter(
    prefix='/hotels',
    tags=['Отели']
)


@router.get("/{location}")
async def get_hotels(
        location: str,
        date_from: datetime,
        date_to: datetime,
) -> list[SGetHotel]:
    result = await HotelsDAO.find_all(location=location)
    return result
