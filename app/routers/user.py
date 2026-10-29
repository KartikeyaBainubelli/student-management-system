from fastapi import APIRouter,HTTPException,Depends,status
from .. import models,schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..utils import hash_password,verify_password


router=APIRouter()

#create user
@router.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(data:schemas.UserCreate,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==data.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="this user already exists")
    
    hashed_password=hash_password(data.password)
    new_user=models.User(
        email=data.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user