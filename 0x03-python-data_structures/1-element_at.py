#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    return my_list[idx]
