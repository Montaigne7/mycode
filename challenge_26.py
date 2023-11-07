#!/usr/bin/env python3

'''Written by Tony
    shows user information upon requested query'''

def main():

    # create a list with characters
    marvelchars = {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
        }
    
    char_name = input(f"Which character do you want to know about?\n{(list(marvelchars.keys()))}\n")

    char_stat = input(f"What statistic do you want to know about?/n {(char_name.keys(marvelchars.get(char_name)))} \n ")

main()

