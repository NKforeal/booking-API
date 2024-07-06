

from app.DAO.base import BaseDAO

from app.hotels.models import Hotels


class HotelsDAO(BaseDAO):
    model = Hotels
