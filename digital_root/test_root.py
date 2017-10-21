"""Test the functionality of digital_root."""

import pytest

from root import digital_root


def test_basic():
    """Basic unit tests provided by codewars."""
    assert digital_root(16) == 7
    assert digital_root(195) == 6
    assert digital_root(992) == 2
    assert digital_root(999999999999) == 9
    assert digital_root(167346) == 9
    assert digital_root(0) == 0


def test_output_exists():
    """Test that an output exists."""
    assert digital_root(2456) is not None


def test_output_type():
    """Test that the output is the type expected."""
    assert type(digital_root(35)) is int


def test_inputs_are_needed():
    """Test that the function will throw an error without inputs."""
    with pytest.raises(TypeError):
        digital_root()


def test_only_nums_are_valid_inputs():
    """Test that only ints are valid inputs."""
    bad_inputs = [["boop", "boink"], 99.99, {"one": 2, "three:": 4}]

    for input in bad_inputs:
        with pytest.raises(ValueError):
            digital_root(bad_inputs)
