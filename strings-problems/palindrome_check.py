"""
Palindrome Check
O(n) time | O(1) space
"""

def palindrome_check(string):
    """
    >>> palindrome_check("racecar")
    True

    >>> palindrome_check("this will fail")
    False
    """
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()