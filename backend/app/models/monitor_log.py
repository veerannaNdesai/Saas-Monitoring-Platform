
from app.db.database import Base
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Mapped , mapped_column ,relationship
from sqlalchemy import ForeignKey

class MonitorLog(Base):
    __tablename__ = "monitor_logs"

    id : Mapped[int] = mapped_column(primary_key=True)

    monitor_id : Mapped[int] = mapped_column(ForeignKey('monitors.id'))

    status : Mapped[str] = mapped_column(default='PENDING')

    response_time : Mapped[int | None] = mapped_column(nullable=True)

    monitor : Mapped['Monitor'] = relationship(
        back_populates = 'monitor_logs'
    )