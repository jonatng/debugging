# Unit Tests

# Test Data
@pytest.fixture
def sample_numbers():
    #Fixture that provides a list of sample numbers
    return [(2, 3, 5), (-1, 1, 0), (0, 0, 0)]

### Sample unit Tests to execute
import pytest
from bugs import add, calculate_average

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

### Bug Fixes
@pytest.mark.edge
def test_calculate_average():
    assert calculate_average([1, 2, 3]) == 2.0
    assert calculate_average([4, 5, 6]) == 5.0
    assert calculate_average([]) == None