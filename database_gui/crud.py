#-----------------------------------------------------------------------------
# This class has CRUD methods
#-----------------------------------------------------------------------------              
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class DbApp:
    def __init__(self):
        print('Constructor Method')
        
    def open_connection(self):
        try:
          self.connection = psycopg2.connect(database=os.environ["DB"], user=os.environ["DB_USERNAME"],
                        password= os.environ["DB_PASS"], host=os.environ["DB_HOST"], port=os.environ["DB_PORT"])
        except (Exception, psycopg2.Error) as error :
            if(self.connection):
                print('Failed to connect to Database', error)
#-----------------------------------------------------------------------------
# Select all Products
#-----------------------------------------------------------------------------                 
    def select_data(self):
        try:
            self.open_connection()
            cursor = self.connection.cursor()
    
            print("Selecting all products")
            sql_select_query = """select * from public."PRODUCT" """
                    
            cursor.execute(sql_select_query)
            records = cursor.fetchall()             
            print(records)
                
    
        except (Exception, psycopg2.Error) as error:
            print('Error in select operation', error)
    
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print('The connection to PostgreSQL was closed.')
        return records
#-----------------------------------------------------------------------------
# Insert Product
#-----------------------------------------------------------------------------                 
    def insert_data(self, code, name, price):
        try:
            self.open_connection()
            cursor = self.connection.cursor()
            postgres_insert_query = """ INSERT INTO public."PRODUCT" 
            ("CODE", NAME, "PRICE") VALUES (%s,%s,%s)"""
            record_to_insert = (code, name, price)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print (count, 'Record successfully inserted into the PRODUCT table')
        except (Exception, psycopg2.Error) as error :
            if(self.connection):
                print('Failed to insert record in PRODUCT table', error)
        finally:
            #closing database connection.
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("The connection to PostgreSQL was closed.")
                
#-----------------------------------------------------------------------------
# Update Product
#-----------------------------------------------------------------------------                 
    def update_data(self, code, name, price):
        try:
            self.open_connection()    
            cursor = self.connection.cursor()

            print('Registration Before Update')
            sql_select_query = """select * from public."PRODUCT" 
            where "CODE" = %s"""
            cursor.execute(sql_select_query, (code,))
            record = cursor.fetchone()
            print(record)    
            # Update record
            sql_update_query = """Update public."PRODUCT" set NAME = %s, 
            "PRICE" = %s where "CODE" = %s"""
            cursor.execute(sql_update_query, (name, price, code))
            self.connection.commit()
            count = cursor.rowcount
            print(count, 'Record updated successfully!')
            print('Record After Update')
            sql_select_query = """select * from public."PRODUCT" 
            where "CODE" = %s"""
            cursor.execute(sql_select_query, (code,))
            record = cursor.fetchone()
            print(record)    
        except (Exception, psycopg2.Error) as error:
            print('Update Error', error)    
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("The connection to PostgreSQL was closed.")

#-----------------------------------------------------------------------------
# Delete Product
#-----------------------------------------------------------------------------                 
    def delete_data(self, code):
        try:
            self.open_connection()    
            cursor = self.connection.cursor()
            sql_delete_query = """Delete from public."PRODUCT" 
            where "CODE" = %s"""
            cursor.execute(sql_delete_query, (code, ))

            self.connection.commit()
            count = cursor.rowcount
            print(count, 'Record deleted successfully!')        
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)    
        finally:
            # closing database connection.
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("The connection to PostgreSQL was closed.")
                
#-----------------------------------------------------------------------------
