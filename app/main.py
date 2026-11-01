from fastapi import FastAPI
from .routers import student,user
from .database import Base,engine
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(
    title="Student Management System",
    description="A REST API for managing student records",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message":"Welcome to STUDENT MANAGEMENT SYSTEM"}


Base.metadata.create_all(bind=engine)
app.include_router(student.router)
app.include_router(user.router)