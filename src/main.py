from fastapi import FastAPI, Query, Body
from pydantic import BaseModel, StrictStr
from typing import List

app = FastAPI()

# Task 1: Personal Info Endpoint
@app.get("/api/v1/me")
def get_user_info():
    return {"name": "蔡昕彤", "student_id": "F74146856"}

# Task 2: Rectangle Area Calculator
@app.get("/api/v1/rectangle/area")
def calculate_rectangle_area(width: int = Query(...), height: int = Query(...)):
    return {"area": width * height}

# Task 3: Word Length Calculator
class WordList(BaseModel):
    words: List[StrictStr]

@app.post("/api/v1/words/lengths")
def calculate_word_lengths(payload: WordList = Body(...)):
    return [{"word": word, "length": len(word)} for word in payload.words]
