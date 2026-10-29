from sqlalchemy import Column,Integer,String,DateTime,func
from .database import Base

class Student(Base):
    __tablename__= "students"
    id=Column(Integer,primary_key=True,index=True)
    full_name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
    age=Column(Integer,nullable=False)
    course=Column(String,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,nullable=False,unique=True)
    hashed_password=Column(String,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
