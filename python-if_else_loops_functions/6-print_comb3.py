#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        # Format both numbers to be two digits
        if i == 8 and j == 9:
            print("{:02d}{:02d}".format(i, j))  # Last pair without comma
        else:
            print("{:02d}{:02d}".format(i, j), end=", ")

