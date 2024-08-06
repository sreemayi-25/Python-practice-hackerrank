# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    ptr=r"^[4-6]\d{3}(-?\d{4}){3}$"
    s=input()
    str=s.replace("-","")
    if (re.search(ptr, s)) and len(str)==16 and not (re.search(r"(\d)\1{3}", str)):
        print("Valid")
    else:
        print("Invalid")
