import mysql.connector

# manages a database connection
class DBConnect:
    # create a DBConnect object for the specified database
    def __init__(self, dbname):
        self.dbname = dbname

    # creates a database connection and returns it
    def connect(self):
        cnx = None

        cnx = mysql.connector.connect(user='root', password='kettlecorn',
                                          host='localhost',
                                          database=self.dbname)
        if cnx.is_connected:
            print("Connection successful")


        return cnx


