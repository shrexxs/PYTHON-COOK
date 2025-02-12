''' 10. Create an array containing the values 1-15, reshape it into a 3-by-5 array, then use indexing and slicing techniques to perform each of the following operations:
'''
import numpy as np

a=np.arange(1,16).reshape(3,5)
print("Original Array:\n", a)

# (a) Select row 2
r2 = a[2, :]
print("\nRow 2:", r2)

# (b) Select column 5
c5 = a[:, 4]
print("\nColumn 5:", c5)

# (c) Select rows 0 and 1
r0_1 = a[0:2, :]
print("\nRows 0 and 1:\n", r0_1)

# (d) Select columns 2-4
c2_4 = a[:, 2:5]
print("\nColumns 2-4:\n", c2_4)

# (e) Select the element that is in row 1 and column 4
eleR1C4 = a[1, 4]
print("\nElement in row 1, column 4:", eleR1C4)

# (f) Select all elements from rows 1 and 2 that are in columns 0, 2, and 4
eleR12_C024 = a[1:3, [0, 2, 4]]
print("\nElements from rows 1 and 2, columns 0, 2, and 4:\n", eleR12_C024)

'''OUTPUTS:
Original Array:
 [[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]]

Row 2: [11 12 13 14 15]

Column 5: [ 5 10 15]

Rows 0 and 1:
 [[ 1  2  3  4  5]
 [ 6  7  8  9 10]]

Columns 2-4:
 [[ 3  4  5]
 [ 8  9 10]
 [13 14 15]]

Element in row 1, column 4: 10

Elements from rows 1 and 2, columns 0, 2, and 4:
 [[ 6  8 10]
 [11 13 15]]
 '''