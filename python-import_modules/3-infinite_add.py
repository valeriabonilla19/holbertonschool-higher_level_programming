#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    for arg in sys.argv[1:]:  # Skip the script name (sys.argv[0])
        total += int(arg)  # Convert each argument to an integer and add it to total
    print(total)
