from fastapi import FastAPI
from .routers import student,user
from .database import Base,engine

app=FastAPI(
    title="Student Management System",
    description="A REST API for managing student records",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message":"Welcome to STUDENT MANAGEMENT SYSTEM"}


Base.metadata.create_all(bind=engine)
app.include_router(student.router)
app.include_router(user.router)