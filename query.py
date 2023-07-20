import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
# mycursor.execute("select * from test2.table_name")
mycursor.execute("select * from test2.table_name where c1 = 123")
for i in mycursor.fetchall():
    print(i)

mydb.close()