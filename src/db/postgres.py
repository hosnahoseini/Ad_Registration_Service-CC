
import sqlalchemy
import databases
import psycopg2


def main():
    conn = psycopg2.connect('postgres://postgres:5w9ervevy7fgkpc@remote.runflare.com:31752/advertisych_db')

    query_sql = """CREATE TABLE Advertisements (
                  id int,
                  description varchar(255),
                  email varchar(255),
                  state varchar(255),
                  category varchar(255)
              );"""

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()
# DATABASE_URL = "postgresql://postgres:5w9ervevy7fgkpc@remote.runflare.com:31752/advertisych_db"

# database = databases.Database(DATABASE_URL)

# metadata = sqlalchemy.MetaData()

# engine = sqlalchemy.create_engine(
#     DATABASE_URL
# )

# advertisements_table = sqlalchemy.Table(
#     "advertisements",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("description", sqlalchemy.String),
#     sqlalchemy.Column("email", sqlalchemy.String),
#     sqlalchemy.Column("state", sqlalchemy.String),
#     sqlalchemy.Column("category", sqlalchemy.String, default=""),
# )

# metadata.create_all(engine)
