from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app3 = FastAPI()

class WordList(BaseModel):
    words: List[str] = Field(..., min_items=1)

@app3.post("/api/v1/word-length-calculator")
def calculate_lengths(payload: WordList):
    return [{"word": word, "length": len(word)} for word in payload.words]
