#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase to uppercase by subtracting 32 from its ASCII value
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))  # Using string formatting with .format() to print the result
