# Write a function that takes a string as a parameter and returns a string with every successive repetitive character replaced with a star(*).

def char_replace(s):
    res=[]
    for i in range(len(s)):
        if i > 0 and s[i] == s[i - 1]:
            res.append('*')
        else:
            res.append(s[i])
    return res
    return ''.join(res)   #join() method takes all items in an iterable and joins them into one string
print(char_replace('balloon'))
 

 #output : bal*o*n
