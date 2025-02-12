#25. Count Digits, Non-Digits, Whitespace, and Words

import re

def count_string_parts(s):
    digits = len(re.findall(r'\d', s))
    non_digits = len(re.findall(r'\D', s))
    whitespace = len(re.findall(r'\s', s))
    words = len(re.findall(r'\w+', s))
    return digits, non_digits, whitespace, words

print(count_string_parts('abc 123 def 456'))  

# Output: (6, 11, 3, 4)