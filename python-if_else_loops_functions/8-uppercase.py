def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase to uppercase
            print(chr(ord(char) - 32), end="")
        else:
            # Print the character as it is
            print(char, end="")
    print()  # Print a newline after the string

