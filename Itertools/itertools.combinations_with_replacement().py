# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
N=input().split(" ")
s=N[0]
s="".join(sorted(s))
n=int(N[1])
l=list(combinations_with_replacement(s,n))
for i in l:
    print("".join(i))
