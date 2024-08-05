import re
n=re.search(r"([a-zA-Z0-9])\1",input())
if n is not None:
    print(n.group(1))
    
else:
    print(-1)
