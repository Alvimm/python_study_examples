from faker import Faker
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
conn = psycopg2.connect(database=os.environ["DB"], user=os.environ["DB_USERNAME"],
                        password= os.environ["DB_PASS"], host=os.environ["DB_HOST"], port=os.environ["DB_PORT"])
print('Connection with database successfully established!')
cur = conn.cursor()
fake = Faker()

n=10
for i in range(n):
    code = i+10
    name_ ='product_'+str(i+1)
    price = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=5, max_value=1000)
    print(price)
    print(name_)
    
    sql_command = """INSERT INTO public. "PRODUCT" ("CODE", "NAME", "PRICE") VALUES (%s, %s, %s)"""
    record = (code,name_,price)
    cur.execute(sql_command, record)

conn.commit() 
cont=cur.rowcount 
print('Insertion successful')
conn.close()