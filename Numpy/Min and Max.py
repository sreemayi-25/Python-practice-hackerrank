import numpy
n,m=[int(x) for x in input().split(" ")]
l=[]
for i in range(n):
    l.append(list(map(int,input().split(" "))))
arr=numpy.array(l)
m=numpy.min(arr,axis=1)
print(numpy.max(m))
    
    
