# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
N=list(input().split(" "))
s=N[0]
s="".join(sorted(s))
n=int(N[1])
l=list(permutations(s,n))
for i in l:
    print("".join(i))
