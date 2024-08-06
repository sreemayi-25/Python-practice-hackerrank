# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    uid=input()
    if len(uid)==10 and uid.isalnum() and len(set(uid))==10 and len(re.findall(r"[A-Z]",uid))>=2 and len(re.findall(r"\d",uid))>=3:
        print("Valid")
    else:
        print("Invalid")
