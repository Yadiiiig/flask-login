import mysql.connector

DB_USER = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = 3306
#DB_PASSWORD = 
DB_DATABASE = 'pentest'

def dbQuery(query, data):
    cnx = mysql.connector.connect(
        user = DB_USER,
        #password = DB_PASSWORD,
        host = DB_HOST,
        port = DB_PORT,
        database = DB_DATABASE
    )
    cursor = cnx.cursor()

    if data:
        cursor.execute(query, data)
        cnx.commit()
        
    cursor.close()
    cnx.close()
    
def dbReturn(query, data):
    cnx = mysql.connector.connect(
        user = DB_USER,
        #password = DB_PASSWORD,
        host = DB_HOST,
        port = DB_PORT,
        database = DB_DATABASE
    )
    cursor = cnx.cursor()

    cursor.execute(query, data)
    result = list(cursor.fetchall())
    
    cursor.close()
    cnx.close()
    return result

def dbReturnNoData(query):
    cnx = mysql.connector.connect(
        user = DB_USER,
        #password = DB_PASSWORD,
        host = DB_HOST,
        port = DB_PORT,
        database = DB_DATABASE
    )
    cursor = cnx.cursor()

    cursor.execute(query)
    result = list(cursor.fetchall())
    
    cursor.close()
    cnx.close()
    return result