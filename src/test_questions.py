"""Test the basic functionality of answer."""

import pytest

from questions import answer


def test_basic():
    """Basic unit tests provided by codewars."""
    assert answer('is khalkhoul dumb', ['no he is NOT', 'i guess so']) == 'no he is NOT'

    possible_answers = [
        'python is a programming language',
        'RAM stands for Random Access Memory',
        'TalonFlame is a pokemon',
        'beeedrill OU',
        'BeeDrill is a pokemon',
        'GNU is not UNIX',
        'biology is boring'
    ]

    test_cases = [
        # (question, expected_answer)
        ('what is python', 'python is a programming language'),
        ('funkiller questions', None),
        ('is beedrill a pokemon', 'BeeDrill is a pokemon'),
        ('what is gnu', 'GNU is not UNIX'),
        ('do you know ANY cool girls', None),
        ('do you like biology too', 'biology is boring')
    ]

    from random import shuffle
    shuffle(test_cases)

    for question, expected in test_cases:
        assert answer(question, possible_answers) == expected


def test_output_exists():
    """Test that an output exists."""
    assert answer('is khalkhoul dumb', ['no he is NOT', 'i guess so']) is not None


def test_output_type():
    """Test that the output is the type expected."""
    assert type(answer('is khalkhoul dumb', ['no he is NOT', 'i guess so'])) is str


def test_inputs_are_needed():
    """Test that the function will throw an error without inputs."""
    with pytest.raises(TypeError):
        answer()


def test_only_nums_are_valid_inputs():
    """Test that only strings or lists are valid inputs."""
    bad_inputs = [12, 56.4, {"one": 2, "three:": 4}]

    for input in bad_inputs:
        with pytest.raises(TypeError):
            answer(input, input, input)
