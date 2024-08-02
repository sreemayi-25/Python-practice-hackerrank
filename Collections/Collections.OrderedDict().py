# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n=int(input())
d=OrderedDict()
for i in range(n):
    item,price=input().rsplit(" ",1)
    price=int(price)
    if item not in d:
        d[item]=price
    else:
        d[item]+=price
for key,value in d.items():
    print(key,value)
