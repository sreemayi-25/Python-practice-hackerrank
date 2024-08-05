# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
pattern=r"(?<=[^aeiou])([aeiou|AEIOU]{2,})(?=[^aeiou])"
match=re.findall(pattern,s)
for i in match:
    print(i)
if not match:
    print(-1)
