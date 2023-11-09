#!/usr/bin/env python3

"""Tony | TLG Learning
    Conditionals - Life of Brian guessing game without a while True loop."""

def main():
    round = 0
    answer = " "

    while round < 3 and answer != "Brian":
        round += 1
        answer = input('Finish the move title, "Monty Python\'s The Life of _____": ')
        if answer.capitalize() == "Brian":
            print("Correct!")
        elif round == 3:
            print("Sorry, the answer was Brian")
        else:
            print("Sorry, Try again!")
        
if __name__ == "__main__":
    main()
