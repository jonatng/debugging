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