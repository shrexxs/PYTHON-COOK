#8. Use linspace and reshape to create a 2-by-3 array with the values 1.1, 2.2, 6.6. Then use astype to convert the array to an array of integers.

import numpy as np

arr = np.linspace(1.1, 6.6, 6).reshape(2, 3)

in_arr = arr.astype(int)

print("Original Array:")
print(arr)
print("\nArray Converted to Integers:")
print(in_arr)


'''OUTPUTS:
Original Array:
[[1.1 2.2 3.3]
 [4.4 5.5 6.6]]

Array Converted to Integers:
[[1 2 3]
 [4 5 6]]
'''