
# pyrefly: ignore [missing-import]
from sqlalchemy.util import deprecated
from passlib.context import CryptContext  
from jose import jwt,JWTError
from datetime import datetime, timedelta, UTC
from fastapi.security import OAuth2PasswordBearer

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
    
def verify_access_token(
    token: str
):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[
                settings.JWT_ALGORITHM
            ]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise ValueError(
                "Invalid token payload"
            )

        return user_id

    except JWTError:
        raise ValueError(
            "Invalid token"
        )

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)









    