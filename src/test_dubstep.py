"""Test the basic functionality of song_decoder."""

import pytest

from dubstep import song_decoder


def test_basic():
    """Basic unit tests provided by codewars."""
    assert song_decoder("AWUBBWUBC") == "A B C"
    assert song_decoder("AWUBWUBWUBBWUBWUBWUBC") == "A B C"
    assert song_decoder("WUBAWUBBWUBCWUB") == "A B C"
    assert song_decoder("RWUBWUBWUBLWUB") == "R L"
    assert song_decoder("WUBJKDWUBWUBWBIRAQKFWUBWUBYEWUBWUBWUBWVWUBWUB") == "JKD WBIRAQKF YE WV"
    assert song_decoder("WUBKSDHEMIXUJWUBWUBRWUBWUBWUBSWUBWUBWUBHWUBWUBWUB") == "KSDHEMIXUJ R S H"
    assert song_decoder("QWUBQQWUBWUBWUBIWUBWUBWWWUBWUBWUBJOPJPBRH") == "Q QQ I WW JOPJPBRH"
    assert song_decoder("WUBWUBOWUBWUBWUBIPVCQAFWYWUBWUBWUBQWUBWUBWUBXHDKCPYKCTWWYWUBWUBWUBVWUBWUBWUBFZWUBWUB") == "O IPVCQAFWY Q XHDKCPYKCTWWY V FZ"
    assert song_decoder("WUBYYRTSMNWUWUBWUBWUBCWUBWUBWUBCWUBWUBWUBFSYUINDWOBVWUBWUBWUBFWUBWUBWUBAUWUBWUBWUBVWUBWUBWUBJB") == "YYRTSMNWU C C FSYUINDWOBV F AU V JB"
    assert song_decoder("WUBKSDHEMIXUJWUBWUBRWUBWUBWUBSWUBWUBWUBHWUBWUBWUB") == "KSDHEMIXUJ R S H"
    assert song_decoder("AWUBWUBWUB") == "A"
    assert song_decoder("AWUBBWUBCWUBD") == "A B C D"
    assert song_decoder("WUBWWUBWUBWUBUWUBWUBBWUB") == "W U B"
    assert song_decoder("WUWUBBWWUBUB") == "WU BW UB"
    assert song_decoder("WUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUABWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUB") == "WUAB"
    assert song_decoder("U") == "U"
    assert song_decoder("WUWUB") == "WU"
    assert song_decoder("UBWUB") == "UB"
    assert song_decoder("WUWUBUBWUBUWUB") == "WU UB U"
    assert song_decoder("WUBWWUBAWUB") == "W A"
    assert song_decoder("WUUUUU") == "WUUUUU"
    assert song_decoder("WUBWUBA") == "A"


def test_output_exists():
    """Test that an output exists."""
    assert song_decoder("WUWUBUBWUBUWUB") is not None


def test_output_type():
    """Test that the output is the type expected."""
    assert type(song_decoder("WUWUBUBWUBUWUB")) is str


def test_inputs_are_needed():
    """Test that the function will throw an error without inputs."""
    with pytest.raises(TypeError):
        song_decoder()


def test_only_nums_are_valid_inputs():
    """Test that only strings are valid inputs."""
    bad_inputs = [["boop", "boink"], 10, 99.99, {"one": 2, "three:": 4}]

    for input in bad_inputs:
        with pytest.raises(AttributeError):
            song_decoder(bad_inputs)
