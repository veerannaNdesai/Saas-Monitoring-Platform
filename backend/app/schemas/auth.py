
from pydantic import BaseModel
from typing import List
from .monitor import MonitorInfo


class RegisterRequest(BaseModel):
    email:str
    password:str


class LoginRequest(BaseModel):
    email:str
    password:str

class TokenResponse(BaseModel):
    access_token:str
    token_type:str

class UserResponse(BaseModel):
    id : int
    email:str

class UserProfileResponse(UserResponse):
    monitors: List[MonitorInfo]
    