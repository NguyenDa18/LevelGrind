"""
Daily Coding Problem #662 [Easy]

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def greatest_gcd(nums):
    """
    >>> greatest_gcd([42, 56, 14])
    14
    """
    greatest_gcd = gcd(nums[0], nums[1])

    for i in range(2, len(nums)):
        greatest_gcd = gcd(greatest_gcd, nums[i])
    return greatest_gcd

if __name__ == "__main__":
    import doctest
    doctest.testmod()
