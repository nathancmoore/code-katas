"""Test the basic functionality of find_smallest_int."""

import sys, pytest

from small import find_smallest_int


def test_basic():
    """Basic unit test provided by codewars."""
    assert find_smallest_int([78, 56, 232, 12, 8]) == 8
    assert find_smallest_int([78, 56, -2, 12, 8]) == -2
    assert find_smallest_int([0, sys.maxint, -1 - sys.maxint]) == -1 - sys.maxint
    assert find_smallest_int([0, sys.maxint, -1 - sys.maxint]) == -1 - sys.maxint
    assert find_smallest_int([-133, -5666, -89, -12341, -321423, sys.maxint]) == -321423
    assert find_smallest_int([0, sys.maxint, -1 - sys.maxint, sys.maxint, sys.maxint]) == -1 - sys.maxint
    assert find_smallest_int([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert find_smallest_int([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -10
    assert find_smallest_int([-78, 56, 232, 12, 8]) == -78
    assert find_smallest_int([78, 56, -2, 12, -8]) == -8


def test_output_exists():
    """Test that an output exists."""
    assert find_smallest_int([78, 56, -2, 12, 8]) is not None


def test_output_type():
    """Test that the output is the type expected."""
    assert type(find_smallest_int([78, 56, -2, 12, 8])) is int


def test_inputs_are_needed():
    """Test that the function will throw an error without inputs."""
    with pytest.raises(TypeError):
        find_smallest_int()


def test_only_nums_are_valid_inputs():
    """Test that only integers or floats are valid inputs."""
    bad_inputs = [["boop", "boink"], "fizz", {"one": 2, "three:": 4}]

    for input in bad_inputs:
        with pytest.raises(TypeError):
            find_smallest_int(input, input, input)
