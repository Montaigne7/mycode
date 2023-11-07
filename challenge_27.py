#!/usr/bin/env python3

"""Challenge 27, Simpons Slicing Challenge!
                        Written by Tony"""

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def main():
    
    # display: My eyes! The goggles do nothing! from the challenge list
    print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")
    a = trial[2]["goggles"]
    b = trial[2]["eyes"]
    c = trial[3]
    # display: My eyes! The goggles do nothing! from the trial list
    print(f"My {a}! The {b} do {trial[3]}!")

main()

