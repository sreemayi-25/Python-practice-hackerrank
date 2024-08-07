import numpy
n,m,p=[int(x) for x in input().split(" ")]
N=[]
M=[]
for i in range(n):
    arr1=list(map(int,input().split(" ")))
    N.append(arr1)
for i in range(m):
    arr2=list(map(int,input().split(" ")))
    M.append(arr2)
res= numpy.concatenate((N,M))
print(res)
