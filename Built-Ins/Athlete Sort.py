n,m=[int(x) for x in input().split(" ")]
arr=[]
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input())
arr.sort(key=lambda x:x[k])
for i in arr:
    print(*i)
