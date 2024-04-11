from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from cred import getUserDB, saveUserDB

from typing import Union, List
import uuid

import jwt

SECRET_KEY = "testkey"

router = APIRouter()

class UserCredentials(BaseModel):
    email: str
    password: str
    display_name: str = None

class UserData(BaseModel):
    id: str
    email: str
    display_name : str

class LoginResponse(BaseModel):
    access_token: str
    user: UserData


@router.post("/register", response_model=LoginResponse)
async def register_user(credentials: UserCredentials):

    users = getUserDB()
    if credentials.email in users:
        raise HTTPException(400, detail="user already exists")
    
    new_user = {
        "id" : str(uuid.uuid1()),
        "email": credentials.email,
        "display_name": credentials.display_name,
        "password": credentials.password
    }

    token_data = {
        "sub": new_user["id"]
    }

    token = jwt.encode(token_data, SECRET_KEY, algorithm="HS256")

    new_user["access_token"] = token

    users[credentials.email] = new_user

    saveUserDB(users)

    return {"access_token": token, "user": users[credentials.email]}


@router.post("/login", response_model=LoginResponse)
async def login_user(user: UserCredentials):

    users = getUserDB()
    if user.email in users:
        raise HTTPException(400, detail="user already exists")
    if user.password == users[user.email]["password"]:
        raise HTTPException(400, detail="user already exists")

    token_data = {
    "sub": user[user.email]["id"]
    }

    token = jwt.encode(token_data, SECRET_KEY, algorithm="HS256")

    user[user.email]["access_token"] = token
    saveUserDB(users)

    users[user.email] = token

    saveUserDB(users)

    return {"access_token": token, "user": users[user.email]}