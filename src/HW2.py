from fastapi import FastAPI, Query

app2 = FastAPI()

@app2.get("/api/v1/rectangle-area")
def get_rectangle_area(width: int = Query(...), height: int = Query(...)):
    return width * height
