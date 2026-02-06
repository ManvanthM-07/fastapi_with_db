from fastapi import APIRouter
from db import get_db
from sqlalchemy.orm import Session
from repositories.User_repo import UserRepo
from fastapi import Depends


router = APIRouter()

@router.post("/signup")
def signup(db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    user_repo.add_user()
    return {"message": "User signed up successfully"}
    

@router.post("/login")
def login():
    return {"message": "User logged in successfully"}