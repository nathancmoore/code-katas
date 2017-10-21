"""For int n input, return the sum of the first nth terms in a series.

#1 Best Practices Solution by MMMAAANNN et al.

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

"""


def series_sum(n):
    """For int n input, return the sum of the first nth terms in a series."""
    total = 0.00
    for i in range(n):
        total += 1.0 / (1.0 + (i * 3.0))
    return "{:0.2f}".format(total)
