"""
Two Sum : Find two numbers in array that sum up to target

>>> two_sum([5, 3, -4, 8, 11, 1, -1, 6], 10)
[-1, 11]
"""

def two_sum(array, target):
    """Test Cases for Two Sum
    >>> two_sum([1,4,8,3,2,9,15], 13)
    [4, 9]
    >>> two_sum([2,7,11,15], 9)
    [2, 7]
    """
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            return [array[left], array[right]]
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
    return []

if __name__ == "__main__":
    import doctest
    doctest.testmod()