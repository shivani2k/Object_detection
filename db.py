import mysql.connector

hostname = 'localhost'
username = 'root'
password = '0909'
database = 'm2'
result = None

def connect():
    myConnection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
    print(myConnection.is_connected())
    myConnection.close()

def insertImage(loc):
    global result
    myConnection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = myConnection.cursor()
    # Preparing SQL query to INSERT a record into the database.
    check_stmt = """SELECT * FROM images WHERE location = %s"""
    insert_stmt = """INSERT INTO images(location) VALUES (%s)"""
    data = (loc,)
    try:
        # Executing the SQL command
        cursor.execute(check_stmt,data)
        res = cursor.fetchall()
        if len(res) != 0:
            deleteEntry(result[0][0])
        cursor.execute(insert_stmt, data)
        # Commit your changes in the database
        myConnection.commit()
        print("Data inserted")
        getHistory()
        return cursor.getlastrowid()
    except Exception as err:
        # Rolling back in case of error
        print(err)
        myConnection.rollback()
    finally:
        myConnection.close()

def getHistory():
    global result
    myConnection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = myConnection.cursor()

    # Preparing SQL query to INSERT a record into the database.
    insert_stmt = """Select * from images"""
    try:
        # Executing the SQL command
        cursor.execute(insert_stmt)
        result = cursor.fetchall()
    except:
        # Rolling back in case of error
        myConnection.rollback()
    finally:
        myConnection.close()

def deleteEntry(id):
    myConnection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = myConnection.cursor()

    # Preparing SQL query to INSERT a record into the database.
    insert_stmt = """DELETE FROM images WHERE id = %s"""
    data = (id,)
    try:
        # Executing the SQL command
        cursor.execute(insert_stmt, data)
        # Commit your changes in the database
        myConnection.commit()
        print("deleted")
    except:
        # Rolling back in case of error
        myConnection.rollback()

    finally:
        myConnection.close()