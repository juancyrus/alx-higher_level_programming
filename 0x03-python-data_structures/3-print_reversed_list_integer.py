#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    reversed = my_list[::-1]
    for numbers in reversed:
        print("{:d}".format(numbers))
