import numpy as np

pow2= np.array([[2**i for i in range (3)]for _ in range(2)])
flat= pow2.flatten()
rav = pow2.ravel()
print(flat)
print(rav)
print(pow2)