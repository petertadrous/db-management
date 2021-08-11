from pymongo import MongoClient
from pymongo import errors as mongoerrors


class DBConnect:
    """Manages a database connection."""
    
    def __init__(self, dbname):
        """Creates a DBConnect object for the specified database.

        Parameters
        ----------
        dbname : str
            the name of the database to connect to
        """
        self.dbname = dbname

    def connect(self):
        """Creates a database connection and returns it.

        Returns
        -------
        MongoClient
            connection to the specified database
        """
        self.client = None
        self.db = None
        try:
            self.client = MongoClient(host="localhost", port=27017)
            self.db = self.client[self.dbname]
        except mongoerrors.ConnectionFailure as e:
            print(e)

        return self.db

    def close(self):
        """Closes the connection to the specified database."""
        self.client.close()


