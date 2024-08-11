import numpy
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(float,input().split(" "))))
arr=numpy.array(l)
print(round(numpy.linalg.det(arr),2))
