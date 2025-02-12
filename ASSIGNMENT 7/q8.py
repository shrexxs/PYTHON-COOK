# Implement a program to check if a string is a valid URL.

import re

def valid_url(url):
    pat = re.compile(r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$')
    return bool(pat.match(url))

print(valid_url('https://www.example.com'))  

# Output: True
