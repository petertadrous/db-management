from pokemon_db_access import *
from pokefields import *

def print_pokemon(pokemon):
    print("----------------------------------")
    print("Our little friend is ", pokemon[NAME], " whose type is ",pokemon[TYPE])
    print("Statistics")
    print("Attack: ", pokemon[ATTACK], " Defense: ", pokemon[DEFENSE])
    moves = pokemon[MOVES]
    for move in moves:
        print(move)

print("**************************************")
print("Retrieving the record for Tentacruel")
pokemon = retrieve_by_name("Tentacruel")
print_pokemon(pokemon)

print("**************************************")
print("Retrieving the Pokemons whose type is electric")
pokemons = retrieve_by_type("electric")
for pokemon in pokemons:
    print_pokemon(pokemon)
print(len(pokemons), " pokemons were returned")

print("**************************************")
print("Retrieving the Pokemons who have the bubble move and the water type")
pokemons = retrieve_by_move_and_type("bubble", "water")
for pokemon in pokemons:
    print_pokemon(pokemon)
print(len(pokemons), " pokemons were returned")

print("**************************************")
print("Retrieving Pokemons whose defense is greater than 75 and attack greater than 80")
pokemons = retrieve_by_defense_and_attack(75,80)
for pokemon in pokemons:
    print_pokemon(pokemon)
print(len(pokemons), " pokemons were returned")

