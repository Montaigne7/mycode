#!/usr/bin/env python3

"""Tony | TLG Learning
    Challenge 50 Lopping for Dracula"""

def main():
    with open("dracula.txt", "r") as book:
        with open("vampytimes.txt", "w") as file:
            count = 0
            for lines in book:
                if "vampire" in lines.lower():
                    count += 1
                    print(lines)
                    file.write(lines)
        print(f'The word "Vampire" appears in the book {count} times')

if __name__ == "__main__":
    main()