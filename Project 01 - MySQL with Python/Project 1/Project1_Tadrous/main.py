import bike_db_access
import kiosk_db_access
import datetime

# Handles most of the logic of the bike rental program Bikes can be checked out
# from a kiosk if the kiosk is not empty. Bikes can be returned to a kiosk if
# the kiosk is not full. Bikes can also be in transit, meaning that the bike is
# not at any kiosk


# check out a bike from a kiosk. If there are no bikes available at the kiosk
# it prints out a message to that effect
# otherwise, it checks out the first bike in the list returned by
# BikeDBAccess.retrieveByKiosk by setting that bike's atKiosk value to 'N'
# and writing that change to the database
def do_checkout():
    print("Enter the kiosk id where you want a bike")
    kid = input()
    num_bikes = bike_db_access.num_bikes_at_kiosk(kid)
    if num_bikes == 0:
        print("This kiosk is empty. You must find another")
    else:
        bike_to_checkout = bike_db_access.retrieve_by_kiosk(kid)[0]
        result = bike_db_access.update(bike_to_checkout.bikeID,
                                       bike_to_checkout.model,
                                       bike_to_checkout.currentKioskID, 
                                       bike_to_checkout.time_arrived,
                                       'N')
        if result:
            print("Bike #{} was checked out from kiosk {} ".format(bike_to_checkout.bikeID,kid))
        else:
            print("There was an error checking out this bike")


# return a bike to a kiosk. If the kiosk is full, it prints out a message
# otherwise, it asks the user for the bike id. If the bike is not in the system
# it prints out an error message. If the bike is already checked in, it also
# prints out an error message. Otherwise it sets the bike's current kiosk id to
# the current kiosk, its time of arrival value to the current date and time
# and its at_kiosk value to 'Y'. It then writes those changes to the database
def do_return():
    print("Enter the kiosk id")
    kid = input()
    kiosk = kiosk_db_access.retrieve_by_kiosk(kid)
    num_bikes = bike_db_access.num_bikes_at_kiosk(kid)
    if num_bikes == kiosk.capacity:
        print("This kiosk is full. You must find another")
    else:
        print("Enter the bike id")
        bike_id = input()
        bike = bike_db_access.retrieve_by_id(bike_id)
        if bike is None:
            print("That bike is not in our system")
            return
        if str.upper(bike.at_kiosk) == 'Y':
            print("This bike is already checked in")
            return
        current_time = datetime.datetime.now()
        result = bike_db_access.update(bike.bikeID, bike.model, kid, current_time, 'Y')
        if result:
            print("Bike #{} was returned to kiosk {} at time {}".format(bike.bikeID,kid, current_time))
        else:
            print("There was an error returning this bike")

# this reads the kiosk id from the user and
# prints out the number of bikes that are currently
# at the kiosk and checked in (at_kiosk = 'Y')
def list_number():
    print("Enter the kiosk id")
    kid = input()
    count = bike_db_access.num_bikes_at_kiosk(kid)
    print(f"There are currently {count} bikes at Kiosk {kid}.")


# this gets the bike id from the user and prints out its kiosk
# if it is checked in and a message that it is in transit if
# it is not currently checked in
def get_location():
    print("Enter the bike id")
    bike_id = input()
    bike = bike_db_access.retrieve_by_id(bike_id)

    if (bike is None):
        print("This bike is not in the system")
        return
    if str.upper(bike.at_kiosk) == 'N':
        print("This bike is in transit")
        return
    else:
        kiosk = kiosk_db_access.retrieve_by_kiosk(bike.currentKioskID)
        print("This bike is located at Kiosk {}, at {}, {}, {} {}.".format(kiosk.kid,
                                                                           kiosk.addr1, 
                                                                           kiosk.city, 
                                                                           kiosk.stat, 
                                                                           kiosk.zip))

# this gets a kiosk id from the user and prints out a report with
# full information on the kiosk and each bike checked into the kiosk
# the bikes are sorted by id
def show_report():
    print("Enter the kiosk id")
    kiosk_id = input ()
    kiosk = kiosk_db_access.retrieve_by_kiosk(kiosk_id)

    if (kiosk is None):
        print("This kiosk is not in the system")
        return

    print("Report for kiosk {}".format(kiosk_id))
    print("Location {}{} {}".format(kiosk.addr1, kiosk.city, kiosk.stat))
    print(datetime.datetime.now())
    bikes = bike_db_access.retrieve_by_kiosk(kiosk_id)
    if len(bikes) == 0:
        print("There are currently no bikes at this kiosk")
    else:
        sorted(bikes,key=lambda bike:bike.bikeID)
        for bike in bikes:
            print("bike id: {} Model {} time arrived {}".format(bike.bikeID, bike.model,bike.time_arrived ))




print("Welcome to the Bike Kiosk Manager")
print("Enter C to checkout a bike, R to return a bike, N to find out the number of bikes at a kiosk, L to find the current location of a bike, S to show the report, Q to quit")
cmd = str.upper(input())

while cmd != 'Q':
    if cmd == 'C':
        do_checkout()
    if cmd == 'R':
        do_return()
    if cmd == 'N':
        list_number()
    if cmd == 'L':
        get_location()
    if cmd == 'S':
        show_report()

    print("Enter C to checkout a bike, R to return a bike, N to find out the number of bikes at a kiosk, L to find the current location of a bike, S to show the report, Q to quit")
    cmd = str.upper(input())

print("Bye!")
