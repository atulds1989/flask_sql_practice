import mysql.connector
import json
from dotenv import load_dotenv
import os

load_dotenv()

hf_key = os.getenv("hf_key")

mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  port=port,
  database=database
)



mycursor = mydb.cursor()


table = 'admin'


create_table_query = f'''
CREATE TABLE IF NOT EXISTS {table} (
    id INT,
    first_name VARCHAR(20),
    last_name VARCHAR(20)
);
'''


mycursor.execute(create_table_query)
mydb.commit()


mycursor.execute(f"select id from {table}")
existing_case = mycursor.fetchall()

if existing_case:
    print(f"record already exists")
else:
    
    insert_query = f''' insert into {table} (id, first_name, last_name) values (%s, %s, %s)'''

    values = [
    (1, 'ASHISH', 'JOHN'),
    (2, 'HIMANSH', 'DAVID')
    ]

    mycursor.executemany(insert_query, values)
    print('record inserted')
    mydb.commit()




select_query = f"SELECT * FROM {table}"

mycursor.execute(select_query)

myresult = mycursor.fetchall()

for row in myresult:
    print(row)




sql = "INSERT INTO admin (ID, FIRST_NAME, LAST_NAME) VALUES (%s, %s,%s)"
values = (3,"Amit","patel")

mycursor.execute(sql, values)
print("new record inserted")



mydb.commit()


table = 'admin'
new_column_name = 'address'
mycursor.execute(f"show columns from {table} like '{new_column_name}'")
existing_column = mycursor.fetchall()

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

mydb.commit()
mydb.close()