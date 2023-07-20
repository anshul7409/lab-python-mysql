import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.table_name values(123,'anshul',234.44,455,'rawat')")
mycursor.execute("insert into test2.table_name values(123,'anshul',234.44,455,'rawat')")
mycursor.execute("insert into test2.table_name values(123,'anshul',234.44,455,'rawat')")
mycursor.execute("insert into test2.table_name values(123,'anshul',234.44,455,'rawat')")
mycursor.execute("insert into test2.table_name values(123,'anshul',234.44,455,'rawat')")
mycursor.execute("insert into test2.table_name values(123,'anshul',234.44,455,'rawat')")
mycursor.execute("insert into test2.table_name values(123,'anshul',234.44,455,'rawat')")
mycursor.execute("insert into test2.table_name values(123,'anshul',234.44,455,'rawat')")
mycursor.execute("insert into test2.table_name values(123,'anshul',234.44,455,'rawat')")

mydb.commit()
mydb.close()