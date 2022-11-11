import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())
conn = psycopg2.connect(database=os.getenv('DB'), user=os.getenv('DB_USERNAME'),
                        password= os.getenv('DB_PASS'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))
print('Connection with database successfully established!')

cur = conn.cursor()
print('Query before upgrade')
cur.execute("""select * from public."phone_book" where "id"=1""")
record = cur.fetchone()
print(record)
# Updating a single record
cur.execute("""Update public."phone_book" set "phone_number"='02188888888' where "id"=1""")
conn.commit()
print("Record Updated Successfully! ")
cur = conn.cursor()
print("Query after update")
cur.execute("""select * from public."phone_book" where "id"=1""")
record=cur.fetchone()
print(record)
conn.commit()
print("Selection successful!")
conn.close()