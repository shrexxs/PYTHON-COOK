#Find the most frequent values in an array of positive integers. The original array is [695175101 55089070765119538796345972702261.

import numpy as np

ar = np.array([6, 9, 5, 1, 7, 5, 1, 0, 1, 5, 5, 0, 8, 9, 0, 7, 0, 7, 6, 5, 1, 1, 9, 5, 3, 8, 7, 9, 6, 3, 4, 5, 9, 7, 2, 7, 0, 2, 2, 6, 1])

u_val, count = np.unique(ar, return_counts=True)

max_c = count.max()

most_fre = u_val[count == max_c]

print("Most Frequent Values:", most_fre)
print("Frequency:", max_c)

"""OUTPUTS :
Most Frequent Values: [5]
Frequency: 7
"""