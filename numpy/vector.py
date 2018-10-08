import numpy as np 
from time import time

a=np.random.rand(10000000) #rank 1 array
b=np.random.rand(10000000)

t0=time()
ab = np.dot(a,b)

print("dot product time:", format(time()-t0, '.5g'),"s")


loop=0
t1=time()
for i in range(10000000):
	loop+=a[i]*b[i]

print("for loop time:", format(time()-t1, '.5g'), "s")
print("the result of ab=",format(ab, '.2g'), "is equal to loop=", format(loop, '.3g'))


# built in functions 
"""
v = vector
np.exp(v)
np.log(v)
np.abs(v)
np.maximum(v,0)
np.sum(x,axis=0)  sum vertically (cols)
np.sum(x,axis=1)  sum horizontally (rows)
v**2
1/v
v.reshape(row,col)
x_norm = np.linalg.norm(x,axis=1,keepdims=True)
"""
