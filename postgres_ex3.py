import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

conn = psycopg2.connect(database=os.getenv('DB'), user=os.getenv('DB_USERNAME'),
                        password= os.getenv('DB_PASS'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))
print('Connection with database successfully established!')
cur = conn.cursor()
cur.execute('''select * from public."phone_book" where "id"=1''')
registration = cur.fetchone()
print(registration)
conn.commit()
print('Selection successfully!')
conn.close()
