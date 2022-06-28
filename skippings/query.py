import simplejson as json
import psycopg2
from psycopg2.extras import RealDictCursor

class PostgresWrapper:


    def __init__(self, **args):
        self.user = args.get('user', 'postgres')
        self.dbname = args.get('dbname', 'skippingsite')
        self.host = args.get('host', 'localhost')
        self.connection = None


    def connect(self):
        pg_conn = psycopg2.connect(
            user=self.user,
            dbname=self.dbname,
            host=self.host
        )
        self.connection = pg_conn


    def get_json_cursor(self):
        return self.connection.cursor(cursor_factory=RealDictCursor)


    @staticmethod
    def execute_and_fetch(cursor, query):
        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        return res

    @staticmethod
    def execute_and_create(cursor, query):
        cursor.execute(query)
        print("record inserted successfully........")


    def get_json_response(self, query):
        cursor = self.get_json_cursor()
        response = self.execute_and_fetch(cursor, query)
        return response


    def get_data(self,query):
        query = query
        return self.get_json_response(query)

    def create_table(self,query):
        conn = psycopg2.connect(
   database="skippingsite", user='postgres', password='', host='localhost', port= ''
)
#Creating a cursor object using the cursor() method
        cursor = conn.cursor()

#Creating table as per requirement
        cursor.execute(query)
        conn.commit()
#Closing the connection
        conn.close()
    








