"""16. Extract Unique Characters in Sorted Order
This function extracts unique characters from a string and returns them sorted."""

def unique_chars_sorted(s):
    return ''.join(sorted(set(s)))

print(unique_chars_sorted('balloon')) 

 # Output: ablno
