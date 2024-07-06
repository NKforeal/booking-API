from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from datetime import datetime

from app.hotels.rooms.model import Rooms


class Hotels(Base):
    __tablename__ = 'hotels'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    services: Mapped[list[str]] = mapped_column(JSON, nullable=True)
    quality: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[str] = mapped_column(nullable=True)

    rooms: Mapped[list["Rooms"]] = relationship(back_populates="hotel", lazy="joined")





