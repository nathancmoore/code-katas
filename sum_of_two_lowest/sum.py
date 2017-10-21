"""Take a list of ints and return the sum of the two smallest.

#1 Best Practices Solution by danman1979 et al.

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
"""


def sum_two_smallest_numbers(numbers):
    """Take a list of ints and return the sum of the two smallest."""
    sorted_list = sorted(numbers)
    return sorted_list[0] + sorted_list[1]
