class bike:
    # create a kiosk object for the specified kiosk
    def __init__(self, bikeID, model, currentKioskID, time_arrived, atKiosk):
        self.bikeID = bikeID
        self.model = model
        self.currentKioskID = currentKioskID
        self.time_arrived = time_arrived
        self.at_kiosk = atKiosk