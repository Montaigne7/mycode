#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print("\nRaw Pokemon Data\n\n", pokeapi)
    print("\nSprite URL:", pokeapi["sprites"]["front_default"])
    print("\nMove Pool:")
    move_num = 0
    for move in pokeapi["moves"]:
        move_num += 1
        move_pool = move["move"]["name"]
        print(f"Move {move_num}: {move_pool}")

    #Without Loop
    game_num = len(pokeapi["game_indices"])
    print(f"\nNumber of Games Appeared: {game_num}")

    #With Loop
    
main()
