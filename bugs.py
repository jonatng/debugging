# Functions for debugging

# This is a simple Python script that adds two numbers
def add(a, b):
    return a + b

# This function calculates the average of a list of numbers
def calculate_average(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

# This function reverses a string
def reverse_string(s):
    return s[::-1]

# This function finds the maximum number in a list
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]  # Initialize with the first number in the list
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# This functions checks if a number is prime
def is_prime(n):
    if n == 1:  # Bug: 1 is not a prime number
        return True
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True
