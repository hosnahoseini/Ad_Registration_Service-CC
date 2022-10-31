
import sqlalchemy
import databases

import psycopg2


def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_q834i3r1maOpS2gxnNN@pg-17c15aea-hosna-34d3.aivencloud.com:26315/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()
# DATABASE_URL = "postgresql://avnadmin:AVNS_q834i3r1maOpS2gxnNN@pg-17c15aea-hosna-34d3.aivencloud.com:26315/defaultdb?sslmode=require"

# database = databases.Database(DATABASE_URL)

# metadata = sqlalchemy.MetaData()

# engine = sqlalchemy.create_engine(
#     DATABASE_URL, pool_size=3, max_overflow=0
# )

# image_table = sqlalchemy.Table(
#     "advertisements",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("description", sqlalchemy.String),
#     sqlalchemy.Column("email", sqlalchemy.String),
#     sqlalchemy.Column("state", sqlalchemy.String),
#     sqlalchemy.Column("category", sqlalchemy.String, default=""),
# )

# metadata.create_all(engine)