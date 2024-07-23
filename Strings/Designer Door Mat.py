# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = [int(x) for x in input().split(' ')]
c = -1
items = []
for i in range(0, n//2):
    c += 2
    items.append(('.|.' * c).center(m, '-'))
for i in items: print(i)    
print('WELCOME'.center(m, '-'))
for i in items[::-1]: print(i)
