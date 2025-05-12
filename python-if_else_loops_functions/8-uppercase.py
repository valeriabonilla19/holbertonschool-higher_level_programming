#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase to uppercase by subtracting 32 from its ASCII value
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()  # Print a new line after the loop
