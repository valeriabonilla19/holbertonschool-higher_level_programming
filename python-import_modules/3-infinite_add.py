#!/usr/bin/python3
import sys

total = 0
for arg in sys.argv[1:]:
    total += int(arg)

# Split the print statement for long results
print(total)
