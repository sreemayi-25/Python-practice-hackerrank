# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N=int(input())
d=deque()
for i in range(N):
    n=list(input().split(" "))
    if n[0]=="append":
        d.append(int(n[1]))
    elif n[0]=="appendleft":
        d.appendleft(int(n[1]))
    elif n[0]=="appendright":
        d.appendright(int(n[1]))
    elif n[0]=="extend":
        d.extend(int(n[1]))
    elif n[0]=="extendleft":
        d.extendleft(int(n[1]))
    elif n[0]=="extendright":
        d.extendright(int(n[1]))
    elif n[0]=="pop":
        d.pop()
    elif n[0]=="popleft":
        d.popleft()
    elif n[0]=="popright":
        d.popright()
for i in d:
    print(i,end=" ")
