from fastapi import APIRouter

router = APIRouter()

@router.get("/signup")
def signup():
    return {"message": "User signed up successfully"}

@router.get("/login")
def login():
    return {"message": "User logged in successfully"}