"""
Daily Coding Problem #626
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

from math import prod
def largest_product(arr):
    """
    >>> arr = [-10, -10, 5, 2]
    >>> largest_product(arr)
    500
    """
    arr.sort(key=abs)
    return prod(arr[-3:])

if __name__ == "__main__":
    import doctest
    doctest.testmod()