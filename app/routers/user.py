from fastapi import APIRouter,HTTPException,Depends,status
from .. import models,schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..utils import hash_password,verify_password
from ..oauth2 import create_access_token,verify_access_token,get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

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

#login user
@router.post("/users/login")
def login(
    data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.email == data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not verify_password(
        data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

