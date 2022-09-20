import sqlite3
from traceback import print_tb

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "akhil", "asdf")

insert_query = "INSERT INTO users VALUES(?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, "amit", "pop"),
    (3, "chris", "hello")
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for i in cursor.execute(select_query):
    print(i)

connection.commit()
connection.close()
