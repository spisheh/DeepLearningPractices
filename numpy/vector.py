import numpy as np 
from time import time

a=np.random.rand(10000000)
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
