"""Test the basic functionality of sum.py."""

import pytest

from sum import sum_two_smallest_numbers


def test_basic():
    """Basic unit tests."""
    assert sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13
    assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19
    assert sum_two_smallest_numbers([25, 42, 12, 18, 22]) == 30
    assert sum_two_smallest_numbers([1, 8, 12, 18, 5]) == 6
    assert sum_two_smallest_numbers([13, 12, 5, 61, 22]) == 17


def test_output_exists():
    """Test that an output exists."""
    assert sum_two_smallest_numbers([5, 8, 12, 18, 22]) is not None


def test_output_type():
    """Test that the output is the type expected."""
    assert type(sum_two_smallest_numbers([5, 8, 12, 18, 22])) is int


def test_inputs_are_needed():
    """Test that the function will throw an error without inputs."""
    with pytest.raises(TypeError):
        sum_two_smallest_numbers()


def test_only_nums_are_valid_inputs():
    """Test that only integers or floats are valid inputs."""
    bad_inputs = [["boop", "boink"], "fizz", {"one": 2, "three:": 4}]

    for input in bad_inputs:
        with pytest.raises(TypeError):
            sum_two_smallest_numbers(bad_inputs)
