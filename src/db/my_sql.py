# import mysql.connector

# HOST = "mysql-33ded920-hosna-34d3.aivencloud.com"
# PORT = 26315
# USER = "avnadmin"
# PASSWORD = "AVNS_qMlnz3Ez4Qmcx86Lsy3"
# DATABASE = "defaultdb"


# mydb = mysql.connector.connect(
#   host = HOST,
#   port = PORT,
#   user = USER,
#   password = PASSWORD,
#   database = DATABASE
# )

# print(mydb)

# mycursor = mydb.cursor()

# mycursor.execute("""CREATE TABLE Persons (
#                   id int,
#                   description varchar(255),
#                   email varchar(255),
#                   state varchar(255),
#                   category varchar(255)
#               );""")

import pymysql

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mysql-33ded920-hosna-34d3.aivencloud.com",
  password="AVNS_qMlnz3Ez4Qmcx86Lsy3",
  read_timeout=timeout,
  port=26315,
  user="avnadmin",
  write_timeout=timeout,
)
  
try:
  cursor = connection.cursor()
  cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
  cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
  cursor.execute("SELECT * FROM mytest")
  print(cursor.fetchall())
finally:
  connection.close()