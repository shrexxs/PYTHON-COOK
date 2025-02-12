#9. Vowels and Consonants Count.This function counts the number of vowels and consonants in a string.

def count_vowels_consonants(s):
    vowels = 'aeiou'
    vowel_count = sum(1 for c in s if c in vowels)
    consonant_count = sum(1 for c in s if c.isalpha() and c not in vowels)
    return vowel_count, consonant_count

print(count_vowels_consonants('hello'))  # Output: (2, 3)
