import mysql.connector
from DBConnect import DBConnect
from bike import bike


def retrieve_by_id(bikeID):
    try:
        dbconnect = DBConnect("bikedb")
        conn = dbconnect.connect()
        cursor = conn.cursor()
        query = "SELECT bikeID, model, currentKioskID, timeArrived, atKiosk from bike where bikeID = %s"
        cursor.execute(query, (bikeID,))
        # print(cursor.statement)
        row = cursor.fetchone()
        if row is None:
            bike_result = None
        else:
            bike_result = bike(*row)

        cursor.close()
        conn.close()
        return bike_result
    except mysql.connector.Error as e:
        print(e)
        return None


def retrieve_by_kiosk(kid):
    try:
        dbconnect = DBConnect("bikedb")
        conn = dbconnect.connect()
        cursor = conn.cursor()
        query = """SELECT
                    bikeID,
                    model,
                    currentKioskID,
                    timeArrived,
                    atKiosk
                   from bike where currentKioskID = %s AND atKiosk = 'Y'"""
        cursor.execute(query, (kid,))

        # print(cursor.statement)

        # this will return multiple rows
        bikes_result = []
        for row in cursor:
            bike_res = bike(*row)
            bikes_result.append(bike_res)

        cursor.close()
        conn.close()
        return bikes_result

    except mysql.connector.Error as e:
        print(e)
        return None

def num_bikes_at_kiosk(kid):
    try:
        dbconnect = DBConnect("bikedb")
        conn = dbconnect.connect()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM bike WHERE currentKioskID = %s AND atKiosk = 'Y'"
        cursor.execute(query, (kid,))
        # print(cursor.statement)
        row = cursor.fetchone()
        if row is None:
            bike_count = None
        else:
            bike_count = row[0]

        cursor.close()
        conn.close()
        return bike_count
    except mysql.connector.Error as e:
        print(e)
        return None

def update(bikeID, bikeModel, kioskID, timestamp, availability):
    try:
        dbconnect = DBConnect("bikedb")
        conn = dbconnect.connect()
        query = """UPDATE bike 
                    SET currentKioskID = %s,
                    timeArrived = %s,
                    atKiosk = %s
                   WHERE bikeID = %s AND model = %s"""
        cursor = conn.cursor()
        cursor.execute(query, (kioskID, timestamp, availability,bikeID,bikeModel))
        conn.commit()
        # print(cursor.statement)
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as e:
        print(e)
        return False