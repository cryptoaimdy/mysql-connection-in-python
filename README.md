# MySQL Integration With Python
The Task is to connect MySQL using python and store data and perform CRUD Operations into it. We ll use one from many special libraries which are used to connect mysql with python applications.

# What is MySQL
MySQL is a database which stores data in tabular form with the help of its Structured query Language. MySQL is a very popular and widely used database.

# What is Python
Python is an Object Oriented Programming Language and is considered very convenient to take in if working on Objects. Python is easy to understand beacuase it has english like syntax and does the work in few lines of code.

Here we ll know about how to connect MySQL in Python using a library called "MySQL Connector". Python has another libraries also to connect MySQL but here we ll use MySQL Connector.

### Technologies Used
+ Used Python3 and Related libraries(MySQL Connector used to connect MySQL database).
+ Used MySQL database 5.7

# Tutorial

**Download and Install MySQL, and then Set Path**

+ Open MySQL in Command Propmt and create a database which u want to link and work through python
Note: You can also use wamp server to create and read your data's into database. Wamp ll show your data in GUI form.


**Libraries to connect mongoDB to Python**
+ MySQL Connector is a great library for MySQL Connectivity.
+ PyMySQL is also a library to connect mysql  with python but we ll prefer mysql connector here here.

We ll Use mysql connector Library.

**IDE Used and version**
+ PyCharm ( PyCharm is recommed IDE for Python, you can use any IDE that supports Python)
+ JetBrains PyCharm Community Edition 2019.1.3
+ Jupiter Notebook is also great for development environment.(Download Anaconda Navigator, 4-5 IDE's are there into that including jupiter notebook)

**Download and install Pycharm IDE**

+ Create a work directory any where on the localmachine(desktop) and open that directory into Pycharm-->Open project.
+ Install mysql connector(a python library for mysql) using "pip install mysql-connector-python" or "pip install mysql-connector-            python==8.0.11" command in the terminal(you can use pycharm terminal also)
+ create a userdata.py file into that directory and import all the required libraries first(mysql connector) then create a connection to Mysql and then create Objects to store in database.

+ Give the Configuration of your mysql server and database name, user and password into userdata.py file. 
 connection = mysql.connector.connect(host='localhost',
                                         database='Cryptocurrencies',
                                         user='root',
                                         password='password')
+ create tables and perform crud operations via code.

# Running the Code!

+ Nowcd to location where
you saved "userdata.py" file and run this command "python userdata.py"
+ Or u can directly click on Run in PyCharm IDE to run the program
