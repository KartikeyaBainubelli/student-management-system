from pydantic import BaseModel,EmailStr,Field,ConfigDict
from typing import Optional
from datetime import datetime

class StudentCreate(BaseModel):
    full_name:str=Field(min_length=2,max_length=100)
    email:EmailStr
    age:int=Field(gt=0,le=120)
    course:str=Field(min_length=2,max_length=100)

class StudentUpdate(BaseModel):
    full_name:Optional[str] =Field(default=None,min_length=2,max_length=100)
    email:Optional[EmailStr]=None
    age:Optional[int]=Field(default=None,gt=0,le=120)
    course:Optional[str]=Field(default=None,min_length=2,max_length=100)

class StudentResponse(BaseModel):
    id:int
    full_name:str
    email:EmailStr
    age:int
    course:str
    created_at:datetime
    
    model_config=ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class UserCreate(BaseModel):
    email:EmailStr
    password:str=Field(min_length=8,max_length=50)

class UserUpdate(BaseModel):
    email:Optional[EmailStr]=None
    password:Optional[str]=Field(min_length=8,max_length=50,default=None)

class UserResponse(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

    model_config = ConfigDict(from_attributes=True)

