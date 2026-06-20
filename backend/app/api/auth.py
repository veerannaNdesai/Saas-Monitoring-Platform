from app.schemas.auth import LoginRequest
from sys import prefix
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.db.database import get_db
from app.schemas.auth import RegisterRequest,LoginRequest
from app.services.auth_service import register_user,login_user
from app.core.dependencies import (
    get_current_user
)

from app.models.user import User
from app.schemas.auth import UserProfileResponse


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
    form_data : OAuth2PasswordRequestForm = Depends(),
    db:Session = Depends(get_db)
):
    request = LoginRequest(email=form_data.username , password=form_data.password)
    return login_user(
        db,request
    )

@router.get(
    "/profile",
    response_model= UserProfileResponse
    )
def profile(
    current_user: User = Depends(
        get_current_user
    )
):
    return current_user