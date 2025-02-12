"""15. Print Substrings with a Particular Frequency
This function prints substrings that appear with a particular frequency."""

def print_substrings_with_freq(s, freq):
    for i in range(len(s) - freq + 1):
        if s[i:i+freq].count(s[i:i+freq][0]) == freq:
            print(s[i:i+freq])

print_substrings_with_freq('aabbbccccddddd', 3)

  # Output: bbb
