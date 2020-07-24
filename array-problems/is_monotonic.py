"""
Monotonic Array : Sorted increasing or decreasing
"""

def is_monotonic(arr):
    """
    >>> is_monotonic([5, 6, 7, 8, 9])
    True

    >>> is_monotonic([4, 9])
    True
    """
    if len(arr) <= 2:
        return True
    i = 0
    while i + 2 < len(arr) - 1:
        first = arr[i]
        mid = arr[i + 1]
        last = arr[i + 2]
        if first <= mid <= last or first >= mid >= last:
            i += 1
        else:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()