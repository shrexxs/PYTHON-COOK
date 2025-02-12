"""13. Remove Extra Spaces Between Words
This function checks for multiple spaces between words and removes them."""

def remove_extra_spaces(sentence):
    return ' '.join(sentence.split())

print(remove_extra_spaces('Hello    World  '))  
# Output: Hello World
