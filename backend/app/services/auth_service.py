import email
from app.db.database import SessionLocal
from app.models.user import User
from app.core.security import hash_password,verify_password,create_access_token
from sqlalchemy.orm import Session  
from app.schemas.auth import RegisterRequest,LoginRequest
from fastapi import HTTPException, status

def register_user(req:RegisterRequest,db:Session):
    existing_user = db.query(User).filter(User.email == req.email).first()

    if existing_user:
        raise HttpException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = hash_password(req.password)

    user = User(
        email = req.email,
        hashed_password = hashed_password
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def login_user(db:Session,req:LoginRequest):
    
    user = db.query(User).filter(User.email==req.email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="user does not exist please register yourself first." 
        )
    
    is_valid = verify_password(req.password,user.hashed_password)

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid password." 
        )
    
    token = create_access_token(
        {
            'sub' : str(user.id)
        }
    )

    return {
    "access_token": token,
    "token_type": "bearer"
}