import numpy
n,m=[int(x) for x in input().split(" ")]
a=numpy.array([input().split() for i in range(n)],int)
b=numpy.array([input().split() for i in range(n)],int)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
