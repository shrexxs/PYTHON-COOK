import numpy as np

a_ev= np.arange(2, 19, 2).reshape(3,3)
a_do= np.arange(9,0,-1).reshape(3,3)
res= a_do * a_ev

print(res)
