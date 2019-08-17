#!/usr/bin/env python
# coding: utf-8

# In[8]:


import mysql.connector
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Cryptocurrencies',
                                         user='root',
                                         password='password')
    
    cursor = connection.cursor()
    sql_update_query = """Update cryptocoins set price_usd = %s where id = %s"""
    # multiple records to be updated in tuple format
    records_to_update = [(3000, 1), (2750, 2)]
    cursor.executemany(sql_update_query, records_to_update)
    connection.commit()
    print(cursor.rowcount, "Records of a cryptocoins table updated successfully")
except mysql.connector.Error as error:
    print("Failed to update records to database: {}".format(error))
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[ ]:




