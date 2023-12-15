import mysql.connector
import json
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("host")
user = os.getenv("root")
password = os.getenv("password")
database = os.getenv("database")
port = os.get_citation("port")



mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  port=port,
  database=database
)



mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM admin")

myresult = mycursor.fetchall()



for row in myresult:
    print(row)

# mydb.commit()


sql = "INSERT INTO admin (ID, FIRST_NAME, LAST_NAME) VALUES (%s, %s,%s)"
values = (3,"Amit","patel")

mycursor.execute(sql, values)



mydb.commit()



new_column_name = 'address'
mycursor.execute(f"show columns from {table} like 'address'")
existing_column = mycursor.fetchone()

if existing_column:
    print(f"the column '{new_column_name}' already exists")

else:
    mycursor.execute(f"ALTER TABLE {table} ADD COLUMN {new_column_name} varchar(20)")
    mydb.commit()




new_column_values = ['Indore', 'Bhopal', 'Jabalpur']

for i, value in enumerate(new_column_values):
    query = f"UPDATE {table} SET address = %s WHERE ID = %s"
    mycursor.execute(query, (value, i+1))  

mydb.commit()


# sql = "DELETE FROM employee WHERE Address = 'BHOPAL'"

# mycursor.execute(sql)

# mydb.commit()
mydb.close()