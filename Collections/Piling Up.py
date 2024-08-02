# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
def func(size,block):
    select=None
    for i in range(size):
        if block[0]>=block[-1]:
            curr=block.popleft()
        else:
            curr=block.pop()
        if select is not None and curr>select:
            return "No"
        select=curr
    return "Yes"
for i in range(int(input())):
    size=int(input())
    block=deque(map(int,input().split()))
    print(func(size,block))
