# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m=[int(x) for x in input().split(" ")]
d=defaultdict(list)
for i in range(n):
    d[input()].append(str(i+1))
for i in range(m):
    ip=input()
    if d[ip]:
        print(" ".join(d[ip]))
    else:
        print(-1)
