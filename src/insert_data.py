#!/usr/bin/env python
# coding: utf-8

# In[22]:


import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   connection = mysql.connector.connect(host='localhost',
                             database='Cryptocurrencies',
                             user='root',
                             password='password')
   sql_insert_query = """ INSERT INTO CryptoCoins
                          (id, name, price_usd, Algo) VALUES (%s,%s,%s,%s)"""
    
   multiple_data = [(1,'Ethereum', 186, 'POS'),
                    (2,'BTC', 12000, 'POW'),
                    (3,'XRP', 0.250, 'RAPC')]

   cursor = connection.cursor()
   cursor.executemany(sql_insert_query, multiple_data)
   connection.commit()
   print ("Record inserted successfully into cryptocoins table")
except mysql.connector.Error as error :
    connection.rollback() #rollback if any exception occured
    print("Failed inserting record into python_users table {}".format(error))
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# In[ ]:




