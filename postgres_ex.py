import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

conn = psycopg2.connect(database=os.getenv('DB'), user=os.getenv('DB_USERNAME'),
                        password= os.getenv('DB_PASS'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))
print('Connection with database successfully established!')
cur = conn.cursor()
cur.execute('''CREATE TABLE phone_book(ID INT PRIMARY KEY NOT NULL,Name TEXT NOT NULL,phone_number CHAR(12));''')
print('Table successfully created!')
conn.commit()
conn.close()
