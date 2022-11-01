# from fastapi import (FastAPI, File, HTTPException, UploadFile)
# from src.db.schema import AdvertiseIn
# from src.RabbitMQ.send import send
# import uvicorn
# from src.db.postgres import advertisements_table, database, engine, metadata
# app = FastAPI(title = "service 1")

# @app.post("/submit_advertisement/")
# async def detect_with_file(description, email, file: UploadFile = File(...)):
#     query = advertisements_table.insert().values(description=description,
#                                                 email=email,
#                                                 state="pending",
#                                                 category="None")

#     id = await database.execute(query=query)
#     # save image on s3
#     # put message on rabbitmq
#     send(id)
#     return f"Your ad was registered with ID: {id}"

# @app.get("/get_advertisement/{id}")
# async def detect_with_file(id:int):
#     query = advertisements_table.select().where(advertisements_table.c.id == id)
#     advertisement = await database.fetch_one(query)

#     if (advertisement.state == "confirmed"):
#         return None
#         # matn, tasvir , dastebandi
#         # return {"category": advertisement.category,
#         #         "description": advertisement.description}

#     if (advertisement.state == "denied"):
#         return "Your ad was not approved"

#     if (advertisement.state == "pending"):
#         return "Your ad is processing"

#     return None



# if __name__ == '__main__':
#     uvicorn.run("main:app",host='188.40.16.3', port=8000, reload=True)


import sqlalchemy
import databases
import psycopg2


def main():
    # conn = psycopg2.connect('postgres://postgres:5w9ervevy7fgkpc@remote.runflare.com:31752/advertisych_db')

    # query_sql = """CREATE TABLE Advertisements (
    #               id int,
    #               description varchar(255),
    #               email varchar(255),
    #               state varchar(255),
    #               category varchar(255)
    #           );"""

    # cur = conn.cursor()
    # cur.execute(query_sql)

    # version = cur.fetchone()[0]
    # print(version)
    DATABASE_URL = "postgresql://postgres:5w9ervevy7fgkpc@remote.runflare.com:31752/advertisych_db"

    database = databases.Database(DATABASE_URL)

    metadata = sqlalchemy.MetaData()

    engine = sqlalchemy.create_engine(
        DATABASE_URL
    )

    advertisements_table = sqlalchemy.Table(
        "advertisements_tb",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("description", sqlalchemy.String),
        sqlalchemy.Column("email", sqlalchemy.String),
        sqlalchemy.Column("state", sqlalchemy.String),
        sqlalchemy.Column("category", sqlalchemy.String, default=""),
    )

    metadata.create_all(engine)
    
    # query = advertisements_table.insert().values(description="foo",
    #                                             email="boo",
    #                                             state="pending",
    #                                             category="None")

    # id = await database.execute(query=query)
    # query = advertisements_table.select().where(advertisements_table.c.id == id)
    # advertisement = await database.fetch_one(query)
    # print(advertisement)


if __name__ == "__main__":
    main()