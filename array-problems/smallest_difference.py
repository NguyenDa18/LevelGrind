"""
O(nlogn + mlogm) time | O(1) space
"""

def smallest_difference(array1, array2):
    arr1, arr2 = sorted(array1), sorted(array2)
    idx1, idx2 = 0, 0
    smallest_diff = float("inf")

    result_pair = []
    while idx1 < len(arr1) and idx2 < len(arr2):
        first_num = arr1[idx1]
        second_num = arr2[idx2]
        current_diff = abs(first_num - second_num)
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            result_pair = [first_num, second_num]
        if first_num <= second_num:
            idx1 += 1
        else:
            idx2 += 1
    return result_pair

result = smallest_difference([1, 2, 3, 4], [4, 3, 2, 1])
print(result)
