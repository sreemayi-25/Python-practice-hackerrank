# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    s=input()
    ptr=r"^[+-]?[0-9]*\.[0-9]+$"
    print(bool(re.search(ptr,s)))
