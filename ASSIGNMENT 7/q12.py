'''12. Generate Three-Letter Strings from Five-Letter Word
This function generates all possible three-letter strings from the given word.'''

from itertools import permutations

def generate_three_letter_strings(word):
    return [''.join(p) for p in permutations(word, 3)]

print(generate_three_letter_strings('bathe'))  

# Output: ['bat', 'bta', 'aht', 'atb', 'the', 'tab']
