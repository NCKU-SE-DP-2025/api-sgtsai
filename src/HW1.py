from fastapi import FastAPI
app1 = FastAPI()
@app1.get("/api/v1/me")
def response():
    return {"name": "蔡昕彤", "student_id": "F74146856"}