# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N=list(input().split(" "))
s=N[0]
s="".join(sorted(s))
n=int(N[1])
l=[]
for i in range(1,n+1):
    l.extend(combinations(s,i))
for i in l:
    print("".join(i))

