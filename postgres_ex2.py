import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

conn = psycopg2.connect(database=os.getenv('DB'), user=os.getenv('DB_USERNAME'),
                        password= os.getenv('DB_PASS'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))
print('Connection with database successfully established!')
cur = conn.cursor()
cur.execute("""INSERT INTO public."AGENDA" ("id", "nome" , "telefone" ) VALUES (1, 'Pessoa 1' , '02199999999' )""")
conn.commit()
print('Insertion successfull')
conn.close()