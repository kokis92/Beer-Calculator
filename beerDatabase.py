#Creating a Microsoft Sql connection with python 
#Python is running the queries from a local host 
from getpass import getpass

import _scproxy
import pymssql  
conn = pymssql.connect(server='localhost', 
    user='sa', 
    password='', 
    database='BeerProject')

# Interacting with the database using a loop 
"""
cursor = conn.cursor(as_dict=True)
cursor.execute('SELECT * FROM Beer WHERE BeerName=%s', 'modelo')
for row in cursor:
    print("BeerID=%d, BeerName=%s , BeerType=%s, Calories=%s, ABV=%s" % (row['BeerID'], 
    row['BeerName'], 
    row['BeerType'],
    row['Calories'],
    row['ABV'] ))

conn.close()
"""


# prints all the Values in the database 
c = conn.cursor(as_dict=True)
# c.execute("SELECT * FROM Beer")
# c.execute("SELECT * FROM BeerStore")
# Inner join two tables Beer table and BeerStore table
# Displays Pacifico Clara beer where packsize is 12
c.execute("Select BeerName, BeerPrice, PackSize, StoreName FROM Beer INNER JOIN BeerStore ON Beer.BeerID = BeerStore.BeerID WHERE BeerName = 'Pacifico Clara' and PackSize = 12")
print(c.fetchall())
conn.commit()


"""
c = conn.cursor(as_dict=True)
c.execute("SELECT b.BeerName, s.BeerPrice, s.PackSize, s.StoreName, MIN(s.BeerPrice) AS LowerPrice
From Beer b 
INNER JOIN BeerStore s ON b.BeerID =s.BeerID
WHere BeerName = 'Pacifico Clara' and PackSize = 12
group by b.BeerName, s.BeerPrice, s.PackSize, s.StoreName
order by s.BeerPrice ASC")
print(c.fetchall())
conn.commit()
"""

