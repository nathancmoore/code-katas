"""Testing module for sort_cards."""

import pytest
from sort_cards import sort_cards
import random

sorted_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

random_decks = [(random.shuffle(sorted_deck), sorted_deck) for i in range(50)]


def test_sort_zero_cards():
    """Sort zero cards."""
    assert sort_cards([]) == []


def test_sort_one_card():
    """Sort one card."""
    assert sort_cards(['5']) == ['5']


def test_sort_cards_list_all_nums():
    """Sort a deck of only numbered cards."""
    assert sort_cards(['3', '2', '7', '9', '8', '4']) == ['2', '3', '4', '7', '8', '9']


def test_sort_cards_list_all_letters():
    """Sort a deck of only face cards."""
    assert sort_cards(['A', 'K', 'Q', 'J']) == ['A', 'J', 'Q', 'K']


@pytest.mark.parameterize("deck, output", random_decks)
def parameterized_shuffled_decks(deck, ordered):
    """100 randomly shuffled decks."""
    assert sort_cards(deck) == ordered
