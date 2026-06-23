from app.models.monitor import Monitor
from app.db.database import Base
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Mapped , mapped_column ,relationship
from sqlalchemy import ForeignKey

class MonitorLog(Base):
    __tablename__ = "monitor_log"

    id = Mapped[int] = mapped_column(primary_key=True)

    monitor_id = Mapped[int] = mapped_column(ForeignKey('monitor.id'))

    status = Mapped[str] = mapped_column(default='PENDING')

    response_time = Mapped[int] | None

    monitor = relationship(
        Monitor,
        back_populates='monitor_log'
    )