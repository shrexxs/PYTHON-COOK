# Write a function that takes two strings and returns True if they are anagrams and False otherwise.
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)   #sorted() returns a sorted list of the specified iterable object

print(are_anagrams('listen', 'silent'))  

# Output: True
