"""Take in a list of numbers and returns the smallest one.

#1 Best Practices Solution by GNX et al.

def findSmallestInt(arr):
    return min(arr)

"""


def find_smallest_int(list_of_nums):
    """Take in a list of numbers and returns the smallest one."""
    return sorted(list_of_nums)[0]
