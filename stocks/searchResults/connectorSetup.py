import mysql.connector

def connect():
    return mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')

def closeConn(conn):
    conn.close()