def gcd(a, b):
    """
    >>> gcd(60, 96)
    12

    >>> gcd(20, 8)
    4
    """
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod()