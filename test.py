import pytest
from Program import process_list

def test_valid_input():
    input_list = list(range(1, 101))  # A list of 100 integers
    result = process_list(input_list)
    expected_length = len(input_list) * (1 - 1/2) * (1 - 1/3) # expected length
    assert len(result) == int(expected_length)

def test_invalid_length():
    with pytest.raises(ValueError, match="🔴 Error: The length of the list must be a multiple of 10."):
        process_list([1, 2, 3, 4, 5])

def test_empty_list():
    assert process_list([]) == []