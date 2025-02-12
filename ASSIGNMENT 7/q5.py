# Write a Python program to find the length of the longest word in a sentence

def long_word(s):
    return max(s.split(),key=len) 
#key=len argument tells max() to use the length of the words as the criteria for determining the maximum.

print(long_word("hey this is shreya mishra speaking , who are you?")) 

#OUTPUT : speaking