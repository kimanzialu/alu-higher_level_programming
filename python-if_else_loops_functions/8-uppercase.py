#!/usr/bin/env python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()  # Print newline after output

