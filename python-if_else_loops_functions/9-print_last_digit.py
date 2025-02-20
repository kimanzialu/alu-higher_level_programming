def print_last_digit(number):
    # Step 1: Get the absolute value of the number and use modulus to get the last digit
    last_digit = abs(number) % 10
    
    # Step 2: Print the last digit (without a new line)
    print(last_digit, end="")
    
    # Step 3: Return the last digit
    return last_digit

