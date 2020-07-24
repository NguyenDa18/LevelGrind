"""
Three Sum : Find all triplets that sum up to target
O(n^2) time | O(n) space
"""

def three_sum(array, targetSum):
    """
    >>> three_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    """
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            sum = array[i] + array[left] + array[right]
            if sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif sum < targetSum:
                left += 1
            elif sum > targetSum:
                right -= 1
    return triplets

if __name__ == "__main__":
    import doctest
    doctest.testmod()