from pymongo import errors as mongoerrors
from db_connect import DBConnect
from kiosk_fields import *


def retrieve_by_kiosk(kiosk_id):
    """Retrieves a Kiosk document by it's ID

    Parameters
    ----------
    kiosk_id : int
        the id of the kiosk to retrieve

    Returns
    -------
    dict
        the kiosk dictionary
    """
    try:
        dbconnect = DBConnect("project2")
        db = dbconnect.connect()
        coll = db.bikekiosks
        query = {KIOSK_ID: kiosk_id}
        kiosk = coll.find_one(query)
        return kiosk
    except mongoerrors.PyMongoError as e:
        print(e)
        return None
    finally:
        if dbconnect != None:
          dbconnect.close()

    
def increment_returns(kiosk_id):
    """Increments the `NUM_RETURNS` of a specified kiosk

    Parameters
    ----------
    kiosk_id : int
        the id of the kiosk to update

    Returns
    -------
    int
        the number of documents updated
    """
    try:
        dbconnect = DBConnect("project2")
        db = dbconnect.connect()
        coll = db.bikekiosks
        query = {KIOSK_ID: kiosk_id}
        newvalues = {"$inc":{NUM_RETURNS: 1}}
        result = coll.update_one(query,newvalues)
        return result.modified_count
    except mongoerrors.PyMongoError as e:
        print(e)
        return 0
    finally:
        if dbconnect != None:
          dbconnect.close()


def increment_checkouts(kiosk_id):
    """Increments the `NUM_CHECKOUTS` of a specified kiosk

    Parameters
    ----------
    kiosk_id : int
        the id of the kiosk to update

    Returns
    -------
    int
        the number of documents updated
    """
    try:
        dbconnect = DBConnect("project2")
        db = dbconnect.connect()
        coll = db.bikekiosks
        query = {KIOSK_ID: kiosk_id}
        newvalues = {"$inc":{NUM_CHECKOUTS: 1}}
        result = coll.update_one(query,newvalues)
        return result.modified_count
    except mongoerrors.PyMongoError as e:
        print(e)
        return 0
    finally:
        if dbconnect != None:
          dbconnect.close()
