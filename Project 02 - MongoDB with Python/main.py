"""Bike Kiosk Manager

Handles most of the logic of the bike rental program. Bikes can be checked out
from a kiosk if the kiosk is not empty. Bikes can be returned to a kiosk if
the kiosk is not full. Bikes can also be in transit, meaning that the bike is
not at any kiosk.
"""

import bike_db_access
import kiosk_db_access
from bike_fields import *
from kiosk_fields import *
import datetime


def main():
    """Main execution section"""
    
    print("Welcome to the Bike Kiosk Manager")
    
    menu_str = """\nEnter:
    \tC to (C)heckout a bike
    \tR to (R)eturn a bike
    \tN to find out the (N)umber of bikes at a kiosk
    \tL to find the current (L)ocation of a bike
    \tS to (S)how the report
    \tQ to (Q)uit"""

    print(menu_str)
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

        print(menu_str)
        cmd = str.upper(input())

    print("Bye!")


def do_checkout():
    """Checks out a bike from a kiosk

    If there are no bikes available at the kiosk, it prints out a
    message to that effect. Otherwise, it checks out the first bike
    in the list returned by bike_db_access.retrieve_by_kiosk by
    setting that bike's atKiosk value to 'N' and writing that change
    to the database. It also increments the numCheckouts value of that
    kiosk using kiosk_db_access.increment_checkouts.
    """
    kiosk_id = int(input("Enter the kiosk id where you want a bike: "))
    num_bikes = bike_db_access.num_bikes_at_kiosk(kiosk_id)
    if num_bikes is None:
        print("That kiosk is not in our system")
        return
    elif num_bikes == 0:
        print("This kiosk is empty. You must find another")
        return
    else:
        bike_to_checkout = bike_db_access.retrieve_by_kiosk(kiosk_id)[0]
        result_of_checkout = bike_db_access.update_checkout(bike_to_checkout[BIKE_ID], 'N')
        if result_of_checkout:
            print("Bike #{} was checked out from kiosk {} ".format(bike_to_checkout[BIKE_ID],kiosk_id))
            result_of_increment = kiosk_db_access.increment_checkouts(kiosk_id)
            if not result_of_increment:
                print('However, there was an error tracking this check out')
        else:
            print("There was an error checking out this bike")


def do_return():
    """Returns a bike to a kiosk

    If the kiosk is full, it prints out a message to that
    effect. Otherwise, it asks the user for the bike id. If the
    bike is not in the system, it prints out an error message.
    If the bike is already checked in, it also prints out an error
    message. Otherwise it sets the bike's current kiosk id to the
    current kiosk, its time of arrival value to the current date and
    time and its atKiosk value to 'Y'. It then writes those changes
    to the database. It also increments the numReturns value of that
    kiosk using kiosk_db_access.increment_returns.
    """
    kiosk_id = int(input("Enter the kiosk id: "))
    kiosk = kiosk_db_access.retrieve_by_kiosk(kiosk_id)
    if kiosk is None:
        print("That kiosk is not in our system")
        return
    num_bikes = bike_db_access.num_bikes_at_kiosk(kiosk_id)
    if num_bikes == kiosk[CAPACITY]:
        print("This kiosk is full. You must find another")
        return
    else:
        bike_id = int(input("Enter the bike id: "))
        bike = bike_db_access.retrieve_by_id(bike_id)
        if bike is None:
            print("That bike is not in our system")
            return
        if str.upper(bike[AT_KIOSK]) == 'Y':
            print("This bike is already checked in")
            return
        current_time = datetime.datetime.now()
        result_of_return = bike_db_access.update_return(
            bike_id=bike[BIKE_ID],
            kiosk_id=kiosk_id,
            time_arrived=current_time,
            at_kiosk='Y')
        if result_of_return:
            print("Bike #{} was returned to kiosk {} at time {}".format(bike[BIKE_ID],kiosk_id,current_time))
            result_of_increment = kiosk_db_access.increment_returns(kiosk_id)
            if not(result_of_increment):
                print('However, there was an error tracking this return')
        else:
            print("There was an error returning this bike")


def list_number():
    """Lists the number of bikes at a kiosk

    This reads the kiosk id from the user and prints out the
    number of bikes that are currently at the kiosk and checked
    in (atKiosk = 'Y').
    """
    kiosk_id = int(input("Enter the kiosk id: "))
    count = bike_db_access.num_bikes_at_kiosk(kiosk_id)
    print(f"There are currently {count} bikes at Kiosk {kiosk_id}.")


def get_location():
    """Prints the current location of a specified bike

    This gets the bike id from the user and prints out its kiosk
    if it is checked in, and a message that it is in transit if
    it is not currently checked in.
    """
    bike_id = int(input("Enter the bike id: "))
    bike = bike_db_access.retrieve_by_id(bike_id)

    if (bike is None):
        print("This bike is not in the system")
        return
    if str.upper(bike[AT_KIOSK]) == 'N':
        print("This bike is in transit")
        return
    else:
        kiosk = kiosk_db_access.retrieve_by_kiosk(bike[CURRENT_KIOSK_ID])
        print("This bike is located at Kiosk {}, at {}, {}, {} {}.".format(kiosk[KIOSK_ID],
                                                                           kiosk[ADDRESS_1], 
                                                                           kiosk[CITY], 
                                                                           kiosk[STATE], 
                                                                           kiosk[ZIP]))


def show_report():
    """Prints a report of a specified kiosk

    This gets a kiosk id from the user and prints out a report with
    full information on the kiosk, the count of each kind of transaction
    at this kiosk, and each bike currently checked into the kiosk with
    the bikes sorted by id.
    """
    kiosk_id = int(input ("Enter the kiosk id: "))
    kiosk = kiosk_db_access.retrieve_by_kiosk(kiosk_id)

    if (kiosk is None):
        print("This kiosk is not in the system")
        return

    print("Report for kiosk {}".format(kiosk_id))
    print("Location {} {} {}".format(kiosk[ADDRESS_1], kiosk[CITY], kiosk[STATE]))
    print(datetime.datetime.now())
    print('Number of checkouts: {}'.format(kiosk[NUM_CHECKOUTS]))
    print('Number of returns: {}'.format(kiosk[NUM_RETURNS]))
    bikes = bike_db_access.retrieve_by_kiosk(kiosk_id)
    if len(bikes) == 0:
        print("There are currently no bikes at this kiosk")
    else:
        sorted(bikes,key=lambda bike:bike[BIKE_ID])
        for bike in bikes:
            print("bike id: {} | Model: {} | time arrived: {}".format(bike[BIKE_ID],bike[MODEL],bike[TIME_ARR]))


if __name__ == '__main__':
    main()
