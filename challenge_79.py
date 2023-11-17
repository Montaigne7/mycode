#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import html
import random

URL= "https://opentdb.com/api.php?amount=3&category=31&difficulty=hard&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data = requests.get(URL).json()
    
    question = html.unescape(data["results"][0]["question"])
    correct = html.unescape(data["results"][0]["correct_answer"])
    incorrect_1 = html.unescape(data["results"][0]["incorrect_answers"][0])
    incorrect_2 = html.unescape(data["results"][0]["incorrect_answers"][1]) 
    incorrect_3 = html.unescape(data["results"][0]["incorrect_answers"][2])

    print(question)
    print

if __name__ == "__main__":
    main()
