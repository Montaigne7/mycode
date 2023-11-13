#!/usr/bin/env python3

"""Written by Tony | TLG Learning
    99 Bottles Song Program"""

def main():
    import time

    for bottles in range(5, 0, -1):
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall! {bottles} \
                              bottles of beer! You take one down pass it \
                              around {bottles} bottles of beer on the wall!")
        elif bottles == 1:
            print(f" {bottles} bottle of beer on the wall! {bottles} bottle \
                               of beer! You take it down pass it around, {bottles} ")
        time.sleep(8)

if __name__ == "__main__":
    main()