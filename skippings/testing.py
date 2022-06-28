import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="skippingsite", user='postgres', password='', host='localhost', port= ''
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Creating table as per requirement
sql ='''
INSERT INTO skippings_product (productname, productimage, productprice) 
           VALUES ('Normal Rope', 'images/normalskipping.jpeg', 100)
'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()