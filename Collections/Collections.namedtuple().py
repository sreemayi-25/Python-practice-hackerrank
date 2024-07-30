# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
heading=input()
students=namedtuple('students',heading)
sum=0
for i in range(n):
    val=input().split()
    s=students(*val)
    sum+=int(s.MARKS)
avg=sum/n
print("%.2f" %avg)
    
    
    
