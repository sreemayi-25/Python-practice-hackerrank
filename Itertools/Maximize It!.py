# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
k,m=map(int,input().split(" "))
l=[]
for i in range(k):
    l.append(list(map(int,input().split(" ")))[1:])
res=max(sum(x**2 for x in value)%m for value in product(*l))
print(res)
