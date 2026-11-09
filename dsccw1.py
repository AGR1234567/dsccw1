import numpy as np

numbers=[11,12,13,14,15]
print(numbers)
for i in range(0,len(numbers)):
    j=numbers[0]*10
    numbers.append(j)
    numbers.pop(0)
print(numbers)
print(type(numbers))

numbers=[1,2,3,4,5]
nparr=np.array(numbers)#make array
print(nparr)
nparrx10=nparr*10
print(nparrx10)
nparr_2=nparr/2
print(nparr_2)
nparr5x0=np.zeros(5,int)
print(nparr5x0)
nparr10x1=np.ones(10,int)
print(nparr10x1)
print(nparr10x1.ndim)#display no of dimentions
print(nparr10x1.shape)#display shape
nparr5x2x1=np.ones((1,5,2))
print(nparr5x2x1)
print(type(nparr))