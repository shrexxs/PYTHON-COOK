''' Write a Python program that checks if a string is a ”rotational palindrome.” A rotational palindrome
 is a string that can be rearranged cyclically to form a palindrome.'''

def ro_palindrome(s):
     s = s.lower()
     for i in range(len(s)):
        rot = s[i:] + s[:i]
        if rot == rot[::-1]:
            return True
     return False

print(ro_palindrome('aabb')) 

 # Output: True