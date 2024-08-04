# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
l=""
u=""
o=""
e=""
for c in s:
    if c.islower():
        l+=c
    elif c.isupper():
        u+=c
    elif c.isdigit():
        if int(c)%2==0:
            e+=c
        else:
            o+=c
L=sorted(l)
U=sorted(u)
O=sorted(o)
E=sorted(e)
print(''.join(L)+''.join(U)+''.join(O)+''.join(E))
