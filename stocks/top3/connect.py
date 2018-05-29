import mysql.connector
from mysql.connector import Error
 
 
def connector():
    """ Connect to MySQL database """
    
    conn = mysql.connector.connect(host='localhost',
                                    database='test',
                                    user='root',
                                    password='')
    return conn
 
