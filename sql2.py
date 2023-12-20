import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("host")
user = os.getenv("root")
password = os.getenv("password")
database = os.getenv("database")
port = os.getenv("port")

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

mycursor.execute(f"SELECT id FROM {table}")
existing_cases = mycursor.fetchall()

if existing_cases:
    print("Records already exist")
else:
    insert_query = f'''INSERT INTO {table} (id, first_name, last_name) VALUES (%s, %s, %s)'''

    values = [
        (1,'ASHISH', 'JOHN'),
        (2,'HIMANSH', 'DAVID')
    ]

    mycursor.executemany(insert_query, values)
    print('Records inserted')
    mydb.commit()

select_query = f"SELECT * FROM {table}"

mycursor.execute(select_query)

myresult = mycursor.fetchall()

for row in myresult:
    print(row)

# Close the cursor and connection when done
mycursor.close()
mydb.close()
