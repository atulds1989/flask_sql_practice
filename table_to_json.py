import mysql.connector, requests
import json
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

mycursor.execute(f"SELECT * FROM {table}")
myresult = mycursor.fetchall()


records_list = []
columns = [column[0] for column in mycursor.description]

# print("columns :\n",columns)

for row in myresult:
    record_dict = dict(zip(columns, row))
    # print(row)
    records_list.append(record_dict)

# print("record dict :\n",record_dict)
# print("record list :\n",records_list)



with open('table_records.json', 'w') as json_file:
    json.dump(records_list, json_file, indent=2)

# Optionally, send the JSON file to the server (replace the server_url with the actual server endpoint)


# server_url = 'https://example.com/upload'
# files = {'file': open('table_records.json', 'rb')}
# response = requests.post(server_url, files=files)

# print("JSON file sent to the server with status code:", response.status_code)

mydb.close()
