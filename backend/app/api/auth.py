from app.schemas.auth import LoginRequest
from sys import prefix
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import RegisterRequest,LoginRequest
from app.services.auth_service import register_user,login_user
from app.core.dependencies import (
    get_current_user
)

from app.models.user import User


router = APIRouter(
    prefix= '/auth',
    tags = ['Authentication']
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    return register_user(
        req=request,
        db=db
    )

@router.post('/login')
def login(
    request:LoginRequest,
    db:Session = Depends(get_db)
):
    return login_user(
        db,request
    )

@router.get("/profile")
def profile(
    current_user: User = Depends(
        get_current_user
    )
):
    return current_user