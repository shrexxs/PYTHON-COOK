import numpy as np

a_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
swap= a_2d[[1,0],:][:,[1,0]]
print(swap)