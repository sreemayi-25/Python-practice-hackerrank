# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
ptr=input()
pattern=re.compile(ptr)
indices=[]
for i in range(len(s)):
    res=pattern.match(s,i)
    if res:
        indices.append((res.start(),res.end()-1))
if indices==[]:
    print((-1,-1))
else:
    for i in indices:
        print(i)
