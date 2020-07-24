def max_subset_sum_with_no_adjacent(array):
    """
    >>> arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    >>> max_subset_sum_with_no_adjacent(arr)
    7
    """
    if not len(array):
        return 0
    if len(array) == 1:
        return array[0]
    max_sum = array[:] # copy array
    max_sum[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + array[i])
    print(max_sum)
    return max_sum[-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
