from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name":"khaled",
        "age":23,
        "job_title": "AI Engineer"
    }
}

class Student(BaseModel):
    name: str
    age: int
    job_title: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    job_title: Optional[str] = None

@app.get("/")
def index():
    return {"name": "test"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Exist"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student doesn't exist"}
    
    if student.name != None:
        students[student_id]["name"] = student.name

    if student.age != None:
        students[student_id]["age"] = student.age

    if student.job_title != None:
        students[student_id]["job_title"] = student.job_title
    
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student doesn't exist"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully"}