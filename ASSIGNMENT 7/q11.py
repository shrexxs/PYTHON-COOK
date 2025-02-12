#11. Find Words Starting and Ending with Specific Letters. This function filters words starting with 'b' and ending with 'd'.

def words_b_to_d(sentence):
    tokens = sentence.split()
    return [word for word in tokens if word.startswith('b') and word.endswith('d')]

print(words_b_to_d('bird band bland bnd'))  # Output: ['bird', 'band']
