# Enter your code here. Read input from STDIN. Print output to STDOUT
s,n=list(map(int,input().split(" ")))
scores=[]
for i in range(n):
    scores.append(map(float,input().split(" ")))
zipscore=zip(*scores)
avg=lambda i:sum(i)/n
for i in zipscore:
    print(avg(i))

