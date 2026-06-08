
# pyrefly: ignore [missing-import]
from sqlalchemy.util import deprecated
from passlib.context import CryptContext  
from jose import jwt
from datetime import datetime, timedelta, UTC

from app.core.config import settings


pwd_context = CryptContext(
        schemes = ['bcrypt'],
        deprecated = 'auto'
)


def hash_password(password:str) -> str:
    return pwd_context.hash(password)



def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password,hashed_password)



def create_access_token(data:dict):
    expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    to_encode['exp'] = expire
    encoded_jwt = jwt.encode(to_encode,settings.JWT_SECRET_KEY,settings.JWT_ALGORITHM)

    return encoded_jwt
    
    

    