from pymongo import MongoClient
from pymongo import errors as mongoerrors


# manages a database connection
class DBConnect:
    # create a DBConnect object for the specified database
    def __init__(self, dbname):
        self.dbname = dbname

    # creates a database connection and returns it
    def connect(self):
        self.client = None
        self.db = None
        try:
            self.client = MongoClient(host="localhost", port=27017)
            self.db = self.client[self.dbname]
        except mongoerrors.errors.ConnectionFailure as e:
            print(e)

        return self.db

    def close(self):
        self.client.close()


