#Creating a Microsoft Sql connection with python 
#Python is running the queries from a local host 
import _scproxy
import pymssql  
conn = pymssql.connect(server='localhost', 
    user='sa', 
    password='Reyes2356', 
    database='BeerProject')

# Interacting with the database 
cursor = conn.cursor(as_dict=True)
cursor.execute('SELECT * FROM Beer WHERE BeerName=%s', 'modelo')
for row in cursor:
    print("BeerID=%d, BeerName=%s , BeerType=%s, Calories=%s, ABV=%s" % (row['BeerID'], 
    row['BeerName'], 
    row['BeerType'],
    row['Calories'],
    row['ABV'] ))

conn.close()


