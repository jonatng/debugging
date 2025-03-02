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

# This function merges two lists and sorts them
def merge_lists(list1, list2):
    return sorted(list1 + list2)
print(merge_lists)

# This function counts the number of vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# This function removes duplicates from a list
def remove_duplicates(x):
    return sorted(dict.fromkeys(x))

# This function checks if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    for i in range(len(s) // 2): # This loop ensures that we only iterate halfway through the string since a palindrome check requires comparing symmetric pairs from the start and end.
        if s[i] != s[-i-1]:  # Bug: Incorrect indexing
            print(f"'{s}' is not a palindrome")
            return False
    print(f"'{s}' is a palindrome")
    return True

# This function counts the number of words in a sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)  
