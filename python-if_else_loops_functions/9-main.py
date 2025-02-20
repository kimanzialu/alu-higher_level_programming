#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

# Test cases
print_last_digit(98)  # Expecting 8
print_last_digit(0)   # Expecting 0
r = print_last_digit(-1024)  # Expecting 4
print(r)  # Should print 4 (value returned by the function)

