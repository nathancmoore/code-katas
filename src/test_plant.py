"""Test the functionality of plant.py."""

import pytest

from plant import growing_plant


def test_basic():
    """Basic unit tests."""
    assert growing_plant(100, 10, 910) == 10
    assert growing_plant(10, 9, 4) == 1
    assert growing_plant(5, 2, 5) == 1
    assert growing_plant(5, 2, 6) == 2


def test_output_exists():
    """Test that an output exists."""
    assert growing_plant(10, 9, 4) is not None


def test_output_type():
    """Test that the output is the type expected."""
    assert type(growing_plant(10, 9, 4)) is int


def test_inputs_are_needed():
    """Test that the function will throw an error without inputs."""
    with pytest.raises(TypeError):
        growing_plant()


def test_only_nums_are_valid_inputs():
    """Test that only integers or floats are valid inputs."""
    bad_inputs = [["boop", "boink"], "fizz", {"one": 2, "three:": 4}]

    for input in bad_inputs:
        with pytest.raises(TypeError):
            growing_plant(input, input, input)
