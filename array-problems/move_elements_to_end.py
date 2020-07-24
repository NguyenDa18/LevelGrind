def move_element_to_end(array, toMove):
    left, right = 0, len(array) - 1
    while left < right:
        if array[right] == toMove:
            right -= 1
        if array[left] != toMove:
            left += 1
        if array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]
    return array

result = move_element_to_end([3, 5, 7, 9, 11], 5)
print(result)