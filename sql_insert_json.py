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

# Read JSON file
with open('demoJson.json') as json_file:
    data = json.load(json_file)

# Insert values from JSON into the table
for record in data:
    sql = "INSERT INTO admin (ID, FIRST_NAME, LAST_NAME, address) VALUES (%s, %s, %s, %s)"
    values = (record["ID"], record["FIRST_NAME"], record["LAST_NAME"], record["address"])
    mycursor.execute(sql, values)

mydb.commit()

# Print the updated table
mycursor.execute("SELECT * FROM admin")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

mydb.close()
