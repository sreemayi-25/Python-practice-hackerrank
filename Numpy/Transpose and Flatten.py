import numpy
n,m=[int(x) for x in input().split(" ")]
l=[]
for i in range(n):
    l.append(list(map(int,input().split(" "))))
arr=numpy.array(l)
print(numpy.transpose(arr))
print(arr.flatten())
