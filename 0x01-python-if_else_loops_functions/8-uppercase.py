#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is lowercase
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end="")
        else:
            # Print the character as is
            print(char, end="")
    
    print()  # Print a newline at the end
