'''  Write a Python function that takes a string and returns a new string where every vowel in the input
 string is replaced by the next vowel in sequence (a → e, e → i, i → o, o → u, u → a).'''

def replace_vowels(s):
    vo = 'aeiou'
    rep = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
    return ''.join([rep[c] if c in vo else c for c in s])

print(replace_vowels('hello'))  # Output: hillu
