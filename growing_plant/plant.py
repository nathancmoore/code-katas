"""Return the number of days for a plant to grow to a certain height.

#1 Best Practices Solution by Giacomo Sorbi

from math import ceil; growing_plant=lambda u,d,h: max([ceil((h-u)/(u-d)),0])+1

"""


def growing_plant(up_speed, down_speed, desired_height):
    """Return the number of days for a plant to grow to a certain height."""
    height = 0
    days = 0
    while height < desired_height:
        days += 1
        height += up_speed
        if height >= desired_height:
            return days
        height -= down_speed
