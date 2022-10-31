from fastapi import (FastAPI, File, HTTPException, UploadFile)
from src.db.schema import AdvertiseIn
import uvicorn

app = FastAPI(title = "service 1")

@app.post("/submit_advertisement/")
async def detect_with_file(payload: AdvertiseIn, file: UploadFile = File(...)):
    return None

@app.post("/submit_advertisement/{name}{description}{email}")
async def detect_with_file(name, description, email, file: UploadFile = File(...)):
    return None

@app.get("/get_advertisement/{id}")
async def detect_with_file(id:int):
    return None

if __name__ == '__main__':
    uvicorn.run("api:app",host='localhost', port=8000, reload=True, debug=True)