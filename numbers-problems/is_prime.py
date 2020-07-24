from math import sqrt

def is_prime(num):
    """
    >>> is_prime(49)
    False
    """
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
