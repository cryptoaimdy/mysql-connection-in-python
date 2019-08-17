#!/usr/bin/env python
# coding: utf-8

# In[8]:


import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   connection = mysql.connector.connect(host='localhost',
                             database='Cryptocurrencies',
                             user='root',
                             password='natural786')
   sql_select_query = "SELECT * from Cryptocoins"

   cursor = connection.cursor()
   cursor.execute(sql_select_query)
   records = cursor.fetchall()
   connection.commit()
   print("Total number of rows in Laptop is: ", cursor.rowcount)
   print("\nPrinting each cryptocoins record")
   for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")


# In[ ]:




