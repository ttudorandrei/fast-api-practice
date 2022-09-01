from fastapi import FastAPI, Path

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

@app.get("/get-student/{student_id}")
# using path here is adding a description of the required query param (in this case, student-id)
def get_Student(student_id: int = Path(None, description="ID of the student you want to see")):
  try:
     return students[student_id]
  except:
    return {"No student with such an id"}
