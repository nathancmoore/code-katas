"""Take in an integer n and return its digital root.

#1 Best Practices Solution by colbydouph et al.

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
"""


def digital_root(n):
    """Take in an integer n and return its digital root."""
    string_n = str(n)
    while len(string_n) > 1:
        sum = 0
        for digit in list(string_n):
            sum += int(digit)

        string_n = str(sum)

    return int(string_n)
