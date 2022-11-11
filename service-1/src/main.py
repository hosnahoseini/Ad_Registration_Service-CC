
from typing import Union

import cv2
from fastapi import FastAPI, File, HTTPException, Response, UploadFile
import uvicorn

from src.api.rabbitmq import send
from src.api.s3 import download_file, upload_file
from src.db.postgres import advertisements_table, database, engine, metadata

app = FastAPI(title = "service 1")

@app.on_event("startup")
async def startup():
    await database.connect()
    

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/submit_advertisement/")
async def submit_advertisement(description, email, file: UploadFile = File(...)):
    
    # insert to db
    query = advertisements_table.insert().values(description=description,
                                                email=email,
                                                state="pending",
                                                category="None",
                                                address="")

    id = await database.execute(query=query)
    address = str(id) + "." + file.filename.split(".")[-1]
    await update_advertisement(id, address=address)

    # save image on s3
    upload_file(file, address)

    # put message on rabbitmq
    send(address)
    return f"Your ad was registered with ID: {id}"

@app.get("/get_advertisement_output/{id}")
async def get_advertisement(id:int):
    query = advertisements_table.select().where(advertisements_table.c.id == id)
    advertisement = await database.fetch_one(query)
    if (advertisement == None):
        return None

    if (advertisement.state == "confirmed"):
        result = {"category": advertisement.category,
                  "description": advertisement.description}
        suffix = advertisement.address.split('.')[-1]
        add = f"./img/output.{suffix}"
        download_file(advertisement.address, add)
        cv2img = cv2.imread(add)
        res, im_png = cv2.imencode(f"output.{suffix}", cv2img)
        response = Response(content = im_png.tobytes(), headers = result, media_type="image/jpg")

        return response

    if (advertisement.state == "denied"):
        return {"result": "Your ad was not approved"}

    if (advertisement.state == "pending"):
        return {"result": "Your ad is processing"}

@app.get("/get_advertisement/{id}")
async def get_advertisement(id:int):
    query = advertisements_table.select().where(advertisements_table.c.id == id)
    advertisement = await database.fetch_one(query)
    return advertisement
    
@app.put("/update_advertisement/")
async def update_advertisement(id:int, state: Union[str, None] = None, category: Union[str, None] = None, address: Union[str, None] = None):
    if(address):
        query = (
            advertisements_table
            .update()
            .where(id == advertisements_table.c.id)
            .values(address=address)
        )
        
    else:
        query = (
            advertisements_table
            .update()
            .where(id == advertisements_table.c.id)
            .values(state=state,
                    category=category)
        )
    await database.execute(query=query)


if __name__ == '__main__':
    uvicorn.run("main:app",host='localhost', port=8000, reload=True)
