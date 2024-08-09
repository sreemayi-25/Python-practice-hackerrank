import numpy
n,m=[int(x) for x in input().split(" ")]
l=[]
for i in range(n):
    l.append(list(map(int,input().split(" "))))
arr=numpy.array(l)
print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(round(numpy.std(arr),11))

    
