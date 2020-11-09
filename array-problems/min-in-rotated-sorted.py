"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""

def min_in_rotated_sorted_array(arr, key):
    """
    >>> arr1 = [5,6,7,8,9,10,1,2,3]
    >>> key = 3
    >>> min_in_rotated_sorted_array(arr1, key)
    8
    """
    size = len(arr)
    pivot = find_pivot(arr, 0, size - 1)

    if pivot == -1:
        return binary_search(arr, 0, size - 1, key)

    # if pivot found then first compare with pivot and then search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binary_search(arr, 0, pivot - 1, key)
    return binary_search(arr, pivot + 1, size - 1, key)


def find_pivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = low + high // 2
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid - 1)
    return find_pivot(arr, mid + 1, high)

def binary_search(arr, low, high, key):
    if high < low:
        return -1
    mid = low + high // 2
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binary_search(arr, mid + 1, high, key)
    if key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod()