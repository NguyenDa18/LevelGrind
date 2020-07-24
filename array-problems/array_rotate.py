"""
Rotate Array
source : https://dxmahata.gitbooks.io/leetcode-python-solutions/content/chapter1.html
"""

def rotate(arr, k):
    """
    My Solution
    """
    return arr[-k:] + arr[:-k]

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))