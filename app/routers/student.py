from fastapi import APIRouter,HTTPException,Depends,status
from .. import models,schemas,oauth2
from ..database import get_db
from sqlalchemy.orm import Session


router=APIRouter()


#get students

@router.get("/students",response_model=list[schemas.StudentResponse])
def get_students(db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    students = db.query(models.Student).filter(models.Student.user_id == current_user.id).all()
    return students

#create student
@router.post("/students",response_model=schemas.StudentResponse,status_code=status.HTTP_201_CREATED)
def create_students(student:schemas.StudentCreate,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    new_student = models.Student(**student.model_dump(),user_id=current_user.id)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

#get a single student
@router.get("/students/{id}",response_model=schemas.StudentResponse)
def get_student(id:int,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    student = db.query(models.Student).filter(models.Student.id == id,models.Student.user_id == current_user.id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id {id} not found ")
    return student

#update students
@router.put("/students/{id}",response_model=schemas.StudentResponse,status_code=status.HTTP_200_OK)
def update_student(id:int,student:schemas.StudentUpdate,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    existing_student = db.query(models.Student).filter(models.Student.id == id,models.Student.user_id == current_user.id).first()
    if existing_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"student with id {id} not found")
    update_data = student.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields provided for update"
        )
    for key, value in update_data.items():
        setattr(existing_student, key, value)
    db.commit()
    db.refresh(existing_student)
    return existing_student

@router.delete("/students/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id:int,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    delete_student = db.query(models.Student).filter(models.Student.id == id,models.Student.user_id == current_user.id).first()
    if delete_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"student with id {id} not found")
    db.delete(delete_student)
    db.commit()
    return