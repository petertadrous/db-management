from pymongo import errors as mongoerrors
from db_connect import DBConnect
from bike_fields import *


def retrieve_by_id(bike_id):
    """Retrieves a bike by it's ID

    Parameters
    ----------
    bike_id : int
        the id of the bike to retrieve

    Returns
    -------
    dict
        the bike with specified id
    """
    try:
        dbconnect = DBConnect("project2")
        db = dbconnect.connect()
        coll = db.bikes
        query = {BIKE_ID: bike_id}
        bike = coll.find_one(query)
        return bike
    except mongoerrors.PyMongoError as e:
        print(e)
        return None
    finally:
        if dbconnect != None:
          dbconnect.close()


def retrieve_by_kiosk(kiosk_id):
    """Retrieves bikes by the kiosk where they are located

    Parameters
    ----------
    kiosk_id : int
        the id of the kiosk to retrieve bikes from

    Returns
    -------
    list
        a list of bikes (dicts) at this kiosk
    """
    try:
        dbconnect = DBConnect("project2")
        db = dbconnect.connect()
        coll = db.bikes
        query = {CURRENT_KIOSK_ID: kiosk_id, AT_KIOSK: 'Y'}
        bikes_list = list(coll.find(query))
        return bikes_list
    except mongoerrors.PyMongoError as e:
        print(e)
        return None
    finally:
        if dbconnect != None:
          dbconnect.close()


def num_bikes_at_kiosk(kiosk_id):
    """Returns the count of bikes at a specified kiosk

    Parameters
    ----------
    kiosk_id : int
        the id of the kiosk the count bikes from

    Returns
    -------
    int
        count of bikes at specified kiosk
    """
    try:
        dbconnect = DBConnect("project2")
        db = dbconnect.connect()
        coll = db.bikes
        query = {CURRENT_KIOSK_ID: kiosk_id, AT_KIOSK: 'Y'}
        num_bikes = coll.count_documents(query)
        return num_bikes
    except mongoerrors.PyMongoError as e:
        print(e)
        return None
    finally:
        if dbconnect != None:
          dbconnect.close()


def update_checkout(bike_id, at_kiosk='N'):
    """Updates a bike document to reflect that it has been checked out

    Parameters
    ----------
    bike_id : int
        the id of the bike to check out
    at_kiosk : str
        the atKiosk status of the bike after checking out, by default 'N'

    Returns
    -------
    int
        the number of documents updated
    """
    try:
        dbconnect = DBConnect("project2")
        db = dbconnect.connect()
        coll = db.bikes
        query = {BIKE_ID: bike_id}
        newvalues = {"$set":{AT_KIOSK: at_kiosk}}
        result = coll.update_one(query,newvalues)
        return result.modified_count
    except mongoerrors.PyMongoError as e:
        print(e)
        return 0
    finally:
        if dbconnect != None:
          dbconnect.close()


def update_return(bike_id, kiosk_id, time_arrived, at_kiosk='Y'):
    """Updates a bike document to reflect that it has been returned

    Parameters
    ----------
    bike_id : int
        the id of the bike being returned
    kiosk_id : int
        the id of the kiosk the bike is being returned to
    time_arrived : datetime
        the date and time the bike was returned
    at_kiosk : str, optional
        the atKiosk status of the bike after returning, by default 'Y'

    Returns
    -------
    int
        the number of documents updated
    """
    try:
        dbconnect = DBConnect("project2")
        db = dbconnect.connect()
        coll = db.bikes
        query = {BIKE_ID: bike_id}
        newvalues = {"$set":{AT_KIOSK: at_kiosk, CURRENT_KIOSK_ID: kiosk_id, TIME_ARR: time_arrived}}
        result = coll.update_one(query,newvalues)
        return result.modified_count
    except mongoerrors.PyMongoError as e:
        print(e)
        return 0
    finally:
        if dbconnect != None:
          dbconnect.close()
