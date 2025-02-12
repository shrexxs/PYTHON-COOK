"""14. Reverse the Middle Half of a String
This function reverses the middle half of a string."""

def reverse_middle_half(s):
    mid = len(s) // 2
    return s[:mid] + s[mid:][::-1]

print(reverse_middle_half('abcdefgh')) 

 # Output: abcdhgfe
