#!/usr/bin/env python3

"""Tony | TLG Learning
    Monty Python movie quiz using conditionals"""

def main():
    round = 0
    while True:
        round = round + 1
        print('Finish the movie title, "Monty Python\'s The Life of _____"')
        answer = input("Your guess --> ")
        if answer == "Brian":
            print("Correct")
            break
        elif round == 3:
            print("Sorry, the answer was Brian")
            break
        else:
            print("Sorry! Try Again!")

if __name__ == "__main__":
    main()


        
        