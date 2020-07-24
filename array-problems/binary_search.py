def binarySearch(array, target):
    """
    >>> binarySearch([0, 4, 5, 6, 7, 3, 8, 9, 10, 11], 11)
    9

    >>> binarySearch([2, 3, 4, 5, 3, 3, 3, 3, 4], 1)
    -1
    """
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod()