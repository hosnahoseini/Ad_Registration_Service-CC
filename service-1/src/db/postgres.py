
import sqlalchemy
import databases
import psycopg2

# DATABASE_URL = "postgres://avnadmin:AVNS_q834i3r1maOpS2gxnNN@pg-17c15aea-hosna-34d3.aivencloud.com:26315/defaultdb?sslmode=require"
# DATABASE_URL = "postgresql://postgres:74dl7agk5s6dt4j@remote.runflare.com:30814/dbkjd_db"
DATABASE_URL = "postgresql://root:Q1H17nu4akny9oHkQFrzIKoW@may.iran.liara.ir:31502/postgres"
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
    sqlalchemy.Column("address", sqlalchemy.String, default=""),

)

metadata.create_all(engine)
