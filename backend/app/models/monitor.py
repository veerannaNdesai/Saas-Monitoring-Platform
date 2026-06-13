
from datetime import datetime
from app.db.database import Base
from sqlalchemy.orm import Mapped , mapped_column ,relationship
from sqlalchemy import ForeignKey


from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.db.database import Base


class Monitor(Base):
    __tablename__ = "monitors"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str]

    url: Mapped[str]

    check_interval: Mapped[int] = mapped_column(
        default=5
    )

    status: Mapped[str] = mapped_column(
        default="PENDING"
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )

    last_checked_at: Mapped[datetime | None] = mapped_column(
        nullable=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="monitors"
    )