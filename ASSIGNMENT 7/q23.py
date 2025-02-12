"""23. Delete the i-th Character"""

def delete_ith_char(s, i):
    return s[:i] + s[i+1:]

print(delete_ith_char('hello', 2)) 

 # Output: helo