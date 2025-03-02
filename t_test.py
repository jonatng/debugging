############## Unit Tests ##############
#                                      #
########################################

############### Test Data ##############

# @pytest.fixture
# def sample_numbers():
#     #Fixture that provides a list of sample numbers
#     return [(2, 3, 5), (-1, 1, 0), (0, 0, 0)]

########## Sample Unit Tests ############
import pytest
from bugs import add, calculate_average, reverse_string, find_max, merge_lists, count_vowels, remove_duplicates, is_palindrome, count_words

@pytest.mark.fast
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
print(test_add)

@pytest.mark.fast
def test_add(sample_numbers):
    # Test add function with predefined data
    for a, b, expected in sample_numbers:
        assert add(a, b) == expected

@pytest.mark.slow
def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

################# Bug Fixes ################

# Fixing the bug in the calculate average function
@pytest.mark.edge
def test_calculate_average():
    assert calculate_average([1, 2, 3]) == 2.0
    assert calculate_average([4, 5, 6]) == 5.0
    assert calculate_average([]) == None

# Fixing the bug in the reverse_string function    
@pytest.mark.edge
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

# Fixing the bug in the find_max function
@pytest.mark.edge
def test_find_max():
    assert find_max([1, 5, 10, 3]) == 10
    assert find_max([-5, -10, -2]) == -2
    assert find_max([]) == None
    
# Fixing the bug in the is_prime function
def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

# Fixing the bug in the merge_lists function
def test_merge_lists():
    assert merge_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_lists([], []) == []
    assert merge_lists([1], [2]) == [1, 2]
    assert merge_lists([1], []) == [1]
    assert merge_lists([], [2]) == [2]
    
# Fixing the bug in the count_vowels function
def test_count_vowels():
    assert count_vowels("Hello") == 2
    assert count_vowels("aeiou") == 5
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0
    assert count_vowels("AEIOU") == 5

# Fixing the bug in the remove_duplicates function
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1]) == [1]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([3, 1, 2, 3, 4, 2, 1]) == [1, 2, 3, 4]

# Fixing the bug in the is_palindrome function
def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    
# Fixing the bug in the count_words function
def test_count_words():
    assert count_words("Hello world this is Python") == 5
    assert count_words("This is a test") == 4
    assert count_words("") == 0
    assert count_words("SingleWord") == 1
    assert count_words("   ") == 0