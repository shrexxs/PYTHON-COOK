'''Write a function format 2d.array (arr) that takes a two-dimensional array of positive integers
 (represented as nested lists)and returns a formatted string that mimics NumPy's column-based format. 
 In this format, each element in the array should be right-aligned, and the width of each column should be 
 determined by the number of characters required to display the largest element in the array.
'''

def format_2d_array(arr):
    
    max_w = max(len(str(element)) for row in arr for element in row)
    formatted_rows = []
    for row in arr:
        formatted_row = " ".join(f"{element:>{max_w}}" for element in row)
        formatted_rows.append(formatted_row)
    return "\n".join(formatted_rows)

array = [
    [1, 22, 333],
    [4444, 555, 66],
    [7, 88, 999]
]

print(format_2d_array(array))

'''OUTPUTS:
   1   22  333
4444  555   66
   7   88  999
'''