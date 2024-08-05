# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    s=input()
    pattern=r"[789]\d{9}$"
    res=re.match(pattern,s)
    if res:
        print("YES")
    else:
        print("NO")
