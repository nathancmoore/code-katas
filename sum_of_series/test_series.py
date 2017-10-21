"""Test the basic functionality of series_sum."""

import pytest

from series import series_sum


def test_basic():
    """Basic unit tests provided by codewars."""
    assert series_sum(1) == "1.00"
    assert series_sum(2) == "1.25"
    assert series_sum(3) == "1.39"
    assert series_sum(4) == "1.49"
    assert series_sum(5) == "1.57"
    assert series_sum(6) == "1.63"
    assert series_sum(7) == "1.68"
    assert series_sum(8) == "1.73"
    assert series_sum(9) == "1.77"
    assert series_sum(15) == "1.94"
    assert series_sum(39) == "2.26"
    assert series_sum(58) == "2.40"
    assert series_sum(0) == "0.00"

    # Test.describe("Random tests")
    # from random import randint
    # sol=lambda n: '0.00' if n==0 else (lambda s: s[:-2]+"."+s[-2:])(str(int(round(sum([1.0/(1+i*3) for i in range(n)])*100))))
    # for _ in range(40):
    #     n=randint(0,100)
    #     Test.it("Testing for "+str(n))
    #     Test.assert_equals(series_sum(n),sol(n),"It should work for random inputs too")


def test_output_exists():
    """Test that an output exists."""
    assert series_sum(6) is not None


def test_output_type():
    """Test that the output is the type expected."""
    assert type(series_sum(6)) is str


def test_inputs_are_needed():
    """Test that the function will throw an error without inputs."""
    with pytest.raises(TypeError):
        series_sum()


def test_only_nums_are_valid_inputs():
    """Test that only integers or floats are valid inputs."""
    bad_inputs = [["boop", "boink"], "fizz", 4.20, {"one": 2, "three:": 4}]

    for input in bad_inputs:
        with pytest.raises(TypeError):
            series_sum(bad_inputs)
