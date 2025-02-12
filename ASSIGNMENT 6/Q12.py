#12. Use NumPy's concatenate Function to reimplement the previous problem.

import numpy as np

a1=np.array([[0,1],[2,3]])
a2=np.array([[4,5],[6,7]])

a3= np.concatenate((a1,a2),axis=0)
print("Vertical Stacking:\n",a3)

a4 = np.concatenate((a1,a2),axis=1)
print("Horizontal Stacking:\n ", a4)

a5 = np.concatenate((a4,a4), axis=0)
print("Vertical Stacking :\n",a5)

a6 = np.concatenate((a3,a3),axis=1)
print("Horizontal Stacking:\n ", a6)

'''OUTPUT:
same output as the question no.11 
{Different Method}
'''

