"""
Array Intersection
source: https://dxmahata.gitbooks.io/leetcode-python-solutions/content/intersection_of_two_arrays.html
"""

def intersection(arr1, arr2):
    """
    >>> intersection([1, 2, 2, 1], [2, 2])
    [2]

    >>> intersection([45, 67, 89, 90, 90], [46, 90, 90, 56, 67])
    [90, 67]

    >>> intersection([1, 1, 0], [7])
    []
    """
    arr1.sort()
    arr2.sort()
    intersection = {}
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            intersection[arr1[i]] = arr1[i]
            i += 1
            j += 1
    return intersection.keys()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)