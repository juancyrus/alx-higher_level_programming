#!/usr/bin/python3
for numbers in range(1, 10):
    for numbers2 in range(numbers+1, 10):
        if numbers == 8 and numbers2 == 9:
            print("{}{}".format(numbers, numbers2))
        else:
            print("{}{}".format(numbers, numbers2), end=", ")
