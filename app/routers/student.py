from fastapi import APIRouter,HTTPException,Depends,status
from .. import models,schemas
from ..database import get_db
from sqlalchemy.orm import Session


router=APIRouter()


#get students

@router.get("/students",response_model=list[schemas.StudentResponse])
def get_students(db:Session=Depends(get_db)):
    students=db.query(models.Student).all()
    return students

#create student
@router.post("/students",response_model=schemas.StudentResponse,status_code=status.HTTP_201_CREATED)
def create_students(student:schemas.StudentCreate,db:Session=Depends(get_db)):
    new_student=models.Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

#get a single student
@router.get("/students/{id}",response_model=schemas.StudentResponse)
def get_student(id:int,db:Session=Depends(get_db)):
    student=db.query(models.Student).filter(models.Student.id==id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id {id} not found ")
    return student

#update students
@router.put("/students/{id}",response_model=schemas.StudentResponse,status_code=status.HTTP_200_OK)
def update_student(id:int,student:schemas.StudentUpdate,db:Session=Depends(get_db)):
    existing_student=db.query(models.Student).filter(models.Student.id==id).first()
    if existing_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"student with id {id} not found")
    update_data = student.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(existing_student, key, value)
    db.commit()
    db.refresh(existing_student)
    return existing_student

@router.delete("/students/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id:int,db:Session=Depends(get_db)):
    delete_student=db.query(models.Student).filter(models.Student.id==id).first()
    if delete_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"student with id {id} not found")
    db.delete(delete_student)
    db.commit()
    return