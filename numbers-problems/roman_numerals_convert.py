"""
Daily Coding Problem #617 (Medium)
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

Source: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html
"""
def int_to_roman_numeral(input):
    """
    >>> int_to_roman_numeral(2002)
    'MMII'

    >>> int_to_roman_numeral(1999)
    'MCMXCIX'
    """
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

def roman_numerals_convert_to_int(input):
    """
    >>> roman_numerals_convert_to_int('XVII')
    17

    >>> roman_numerals_convert_to_int('X')
    10

    >>> roman_numerals_convert_to_int('XLII')
    42
    """
    numerals_values = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
    }
    sum = 0
    for i in range(len(input)):
        value = numerals_values[input[i]]
        # if next place holds larger number, this value is negative
        if i + 1 < len(input) and numerals_values[input[i + 1]] > value:
            sum -= value
        else:
            sum += value
    return sum

if __name__ == "__main__":
    import doctest
    doctest.testmod()