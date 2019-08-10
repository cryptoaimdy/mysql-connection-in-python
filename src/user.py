import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   connection = mysql.connector.connect(host='localhost',
                             database='Cryptocurrencies',
                             user='root',
                             password='password')
   sql_insert_query = """ INSERT INTO `CryptoCoins`
                          (id, name, price_usd, Algo) VALUES (1,'Ethereum', 12000, 'POS')"""
   cursor = connection.cursor()
   result  = cursor.execute(sql_insert_query)
   connection.commit()
   print ("Record inserted successfully into python_users table")
except mysql.connector.Error as error :
    connection.rollback() #rollback if any exception occured
    print("Failed inserting record into python_users table {}".format(error))
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")