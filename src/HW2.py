from fastapi import FastAPI

app2 = FastAPI()

@app2.get("/api/v1/rectangle-area/{width}/{height}")
def get_area(width: int, height: int):
    return {"area": width * height}
