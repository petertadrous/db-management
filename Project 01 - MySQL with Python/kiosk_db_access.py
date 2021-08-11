import mysql.connector
from DBConnect import DBConnect
from kiosk import kiosk

def retrieve_by_kiosk(kid):
    try:
        dbconnect = DBConnect("bikedb")
        conn = dbconnect.connect()
        cursor = conn.cursor()
        query = "SELECT kioskID, addr1, addr2, city, stat, zip, capacity from bikekiosk where kioskID = %s"
        cursor.execute(query, (kid,))
        # print(cursor.statement)
        row = cursor.fetchone()
        if row is None:
            kiosk_result = None
        else:
            kiosk_result = kiosk(*row)

        cursor.close()
        conn.close()
        return kiosk_result
    except mysql.connector.Error as e:
        print(e)
        return None