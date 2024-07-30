# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n=int(input())
l=input().split(" ")
k=int(input())
c=list(combinations(l,k))
s=0
for i in c:
    if "a" in i:
        s+=1
print(s/len(c))
