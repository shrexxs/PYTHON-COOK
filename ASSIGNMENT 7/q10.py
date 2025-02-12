#10. [Tokenize and Reverse Tokens] This function tokenizes the string and outputs the tokens in reverse order.

def reverse_tokens(sentence):
    tokens = sentence.split()
    return ' '.join(tokens[::-1])

print(reverse_tokens('This is a test sentence'))  # Output: sentence test a is This
