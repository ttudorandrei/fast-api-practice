from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
  1: {
    "name":"John",
    "age":17,
    "class": "Year 12"
  }
}

@app.get("/")
def home():
  return {"name": "First Data"}

# using path parameter
@app.get("/get-student/{student_id}")
# using path here is adding a description of the required query param (in this case, student-id)
# gt = greater than, lt = lower than etc
def get_student(student_id: int = Path(None, description="ID of the student you want to see", gt=0, lt=3)):
  try:
     return students[student_id]
  except:
    return {"No student with such an id"}

# using query parameter
@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
  for student_id in students:
    if students[student_id]["name"] == name:
      return students[student_id]
  return {"Data": "Not Found"}