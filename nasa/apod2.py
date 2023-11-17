#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# this is our main function
def main():
    ## make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI)

    ## strip off json
    apod = apodresp.json()

    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()
