from operator import index
from enum import unique
from app.db.database import Base
from sqlalchemy.orm import Mapped,mapped_column


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True,)
    email:Mapped[str] = mapped_column(unique=True,index=True)
    hashed_password:Mapped[str] 
    

    