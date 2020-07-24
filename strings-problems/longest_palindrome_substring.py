def longest_palindrome_substring(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j + 1]
            if len(substring) > len(longest) and is_palindrome(substring):
                longest = substring
    return longest