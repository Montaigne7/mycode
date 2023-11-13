#!/usr/bin/env python3

"""Tony | TLG Learning
    Conditional mini-project"""

def main():
    books = ["Inheritance", "Eldest", "Eragon", "Brisingr"]
    eragon = books[2]
    eldest = books[1]
    brisingr = books[3]
    inheritance = books[0]
    
    print("Please put the Inheritance Cycle books in order:")
    print("    ".join(books))
    
    choice_1 = " "
    attempt = 0

    while attempt < 4 and choice_1 != eragon:
        attempt += 1
        choice_1 = input("What is the first book in the series? ")
        if choice_1.capitalize() == eragon:
            choice_1 = choice_1.capitalize()
            print("That is correct")
        elif attempt == 4:
            print("The first book in the series is", eragon)
        else:
            print("That is incorrect, try again.")
    
    print(eragon)
    choice_2 = " "
    attempt = 0 
    
    while attempt < 4 and choice_2 != eldest:
        attempt += 1
        choice_2 = input("What is the second book in the series? ")
        if choice_2.capitalize() == eldest:
            choice_2 = choice_2.capitalize()
            print("That is correct")
        elif attempt == 4:
            print("The second book in the series is", eldest)
        else:
            print("That is incorrect, try again.")

    print(f"{eragon}, {eldest}")
    choice_3 = " "
    attempt = 0 
    
    while attempt < 4 and choice_3 != brisingr:
        attempt += 1
        choice_3 = input("What is the third book in the series? ")
        if choice_3.capitalize() == brisingr:
            choice_3 = choice_3.capitalize()
            print("That is correct")
        elif attempt == 4:
            print("The third book in the series is", brisingr)
        else:
            print("That is incorrect, try again.")

    print(f"{eragon}, {eldest}, {brisingr}")
    choice_4 = " "
    attempt = 0 
    
    while attempt < 4 and choice_4 != inheritance:
        attempt += 1
        choice_4 = input("What is the fourth book in the series? ")
        if choice_4.capitalize() == inheritance:
            choice_4 = choice_4.capitalize()
            print("That is correct")
        elif attempt == 4:
            print("The fourth book in the series is", inheritance)
        else:
            print("That is incorrect, try again.")

    print(f"{eragon}, {eldest}, {brisingr}, {inheritance}")

if __name__ == "__main__":
    main()
