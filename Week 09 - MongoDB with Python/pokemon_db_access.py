from pymongo import errors as mongoerrors

from db_connect import DBConnect
from pokefields import *

def retrieve_by_name(name):
    try:
        dbconnect = DBConnect("week9")
        db = dbconnect.connect()
        coll = db.pokemon
        query = {NAME: name}
        print("query is", query)
        pokemon = coll.find_one(query)
        return pokemon
    except mongoerrors.PyMongoError as e:
        print(e)
        return None
    finally:
        if dbconnect != None:
          dbconnect.close()

def retrieve_by_type(type):
    try:
        dbconnect = DBConnect("week9")
        db = dbconnect.connect()
        coll = db.pokemon
        query = {TYPE: type}
        print("query is", query)
        pokemon_list = list(coll.find(query))
        return pokemon_list
    except mongoerrors.PyMongoError as e:
        print(e)
        return None
    finally:
        if dbconnect != None:
          dbconnect.close()

def retrieve_by_move_and_type(move,type):
    try:
        dbconnect = DBConnect("week9")
        db = dbconnect.connect()
        coll = db.pokemon
        query = {MOVES: move, TYPE: type}
        print("query is", query)
        pokemon_list = list(coll.find(query))
        return pokemon_list
    except mongoerrors.PyMongoError as e:
        print(e)
        return None
    finally:
        if dbconnect != None:
          dbconnect.close()

def retrieve_by_defense_and_attack(defenseMin,attackMin):
    try:
        dbconnect = DBConnect("week9")
        db = dbconnect.connect()
        coll = db.pokemon
        query = {DEFENSE: {'$gt': defenseMin}, ATTACK: {'$gt': attackMin}}
        print("query is", query)
        pokemon_list = list(coll.find(query))
        return pokemon_list
    except mongoerrors.PyMongoError as e:
        print(e)
        return None
    finally:
        if dbconnect != None:
          dbconnect.close()