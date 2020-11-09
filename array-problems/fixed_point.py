"""
Daily Coding Problem: Problem #708
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
"""

def fixed_point(arr):
    """
    >>> arr = [-6, 0, 2, 40]
    >>> fixed_point(arr)
    2

    >>> arr1 = [1, 5, 7, 8]
    >>> fixed_point(arr1)
    False
    """
    for idx, num in enumerate(arr):
        if num == idx:
            return arr[idx]
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()

