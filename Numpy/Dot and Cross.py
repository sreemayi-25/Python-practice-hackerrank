import numpy
n=int(input())
arr1=[]
arr2=[]
for i in range(n):
    arr1.append(list(map(int,input().split(" "))))
a=numpy.array(arr1)
for i in range(n):
    arr2.append(list(map(int,input().split(" "))))
b=numpy.array(arr2)
print(numpy.dot(a,b))
