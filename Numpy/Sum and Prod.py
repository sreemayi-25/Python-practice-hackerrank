import numpy
n,m=[int(x) for x in input().split(" ")]
l=[]
for i in range(n):
    l.append(list(map(int,input().split(" "))))
arr=numpy.array(l)
s=numpy.sum(arr,axis=0)
prod=numpy.prod(s)
print(prod)
