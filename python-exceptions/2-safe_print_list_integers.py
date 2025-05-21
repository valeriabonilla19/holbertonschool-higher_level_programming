#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip elements that cannot be formatted as integers silently
            pass
        except IndexError:
            # If i goes beyond the list length, break out of the loop
            break
    print()
    return count
