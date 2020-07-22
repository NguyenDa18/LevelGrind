"""
Fibonacci Numbers : Generate the fib for N
"""

def fib(N):
    """Test Cases for Fibonacci
    >>> fib(1)
    1
    >>> fib(4)
    3
    >>> fib(8)
    21
    """
    if N == 0:
        return 0
    last_two = [1, 1]
    counter = 3
    while counter <= N:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1] if N > 1 else last_two[0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()