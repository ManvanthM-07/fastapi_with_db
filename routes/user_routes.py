from fastapi import APIRouter, HTTPException
from db import get_db
from sqlalchemy.orm import Session
from repositories.User_repo import UserRepo
from schemas.User_schemas import UserSchema
from models import User
from fastapi import Depends


router = APIRouter()

#@router.post("/signup")
#def signup(db: Session = Depends(get_db)):
    #user_repo = UserRepo(db)
    #user_repo.add_user()
    #return {"message": "User signed up successfully"}
    
@router.post("/signup")
def signup(user: UserSchema, db: Session = Depends(get_db)):
    User_repo = UserRepo(db)
    existing_user = User_repo.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    # Convert Pydantic schema to SQLAlchemy model
    db_user = User(email=user.email, password=user.password)
    User_repo.add_user(db_user)
    return {"message": "User signed up successfully"}
    

@router.post("/login")
def login():
    return {"message": "User logged in successfully"}