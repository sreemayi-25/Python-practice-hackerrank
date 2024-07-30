# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
N=int(input())
sizes=list(map(int,input().split(" ")))
avail=Counter(sizes)
cust=int(input())
amt=0
for i in range(cust):
    s,p=[int(x) for x in input().split(" ")]
    if s in avail.keys() and avail[s]>0:
        avail[s]=avail[s]-1
        amt+=p
print(amt)
    
    
