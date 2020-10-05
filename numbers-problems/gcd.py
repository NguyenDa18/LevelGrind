def gcd(a, b):
    """
    >>> gcd(60, 96)
    12

    >>> gcd(20, 8)
    4
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod()