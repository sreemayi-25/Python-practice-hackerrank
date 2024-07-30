# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s=input()
string=groupby(s)
l=[]
for i,j in string:
    count=len(list(j))
    l.append("({}, {})".format(count,i))
for i in l:
    print(i,end=" ")
