#!/usr/bin/env python
# coding: utf-8

# In[17]:


import mysql.connector
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Cryptocurrencies',
                                         user='root',
                                         password='natural786')
    
    cursor = connection.cursor()
    print ("Records Before Deleting single record from cryptocoins table")
    sql_select_query = """select * from cryptocoins"""
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    for record in records :
        print (record)
       #Delete record now
    sql_Delete_query = """Delete from cryptocoins where id = 3"""
    cursor.execute(sql_Delete_query)
    connection.commit()
    print ("\nRecord Deleted successfully ")
    print("\nTotal records from cryptocoins table after Deleting single record\n ")
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    for record in records:
        print(record)
except mysql.connector.Error as error :
    print("Failed to delete record: {}".format(error))
finally:
    #closing database connection.
    if(connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# In[ ]:




