from sqlalchemy.orm import relationship
from operator import index
from enum import unique
from app.db.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import ForeignKey


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True,)
    email:Mapped[str] = mapped_column(unique=True,index=True)
    hashed_password:Mapped[str] 
    
    monitors = relationship(
        'Monitor' , 
        back_populates = 'user'
    )

    