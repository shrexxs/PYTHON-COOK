'''11. Given the following 2-dimensional arrays in NumPy:

array1 = np.array([[0, 1], [2, 3]])
array2= np.array([[4, 5], [6, 7]])

Perform the following tasks:
(a) Use vertical stacking to create a 4-by-2 array named array 3, with arrayl stacked on top of array2.
(b) Use horizontal stacking to create a 2-by-4 array named arrays, with array2 to the right of array1.
(c) Use vertical stacking with two copies of array 4 to create a 4-by-4 array named array5.
(d) Use horizontal stacking with two copies of array 3 to create a 4-by-4 array named array6.
'''

import numpy as np

a1=np.array([[0,1],[2,3]])
a2=np.array([[4,5],[6,7]])

a3= np.vstack((a1,a2))
print("Vertical stacking :\n", a3)

a4 = np.hstack((a1,a2))
print("Horizontal Stacking :\n", a4)

a5 = np.vstack((a4,a4))
print("Vertical Stacking of a4 :\n", a5)

a6 = np.hstack((a3,a3))
print("Horizontal Stacking of a3 :\n", a6)

'''OUTPUTS:
Vertical stacking :
 [[0 1]
 [2 3]
 [4 5]
 [6 7]]
Horizontal Stacking :
 [[0 1 4 5]
 [2 3 6 7]]
Vertical Stacking of a4 :
 [[0 1 4 5]
 [2 3 6 7]
 [0 1 4 5]
 [2 3 6 7]]
Horizontal Stacking of a3 : 
[[0 1 0 1]
 [2 3 2 3]
 [4 5 4 5]
 [6 7 6 7]]
'''