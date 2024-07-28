# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
arr=list(map(int,input().split(" ")))
s=set(arr)
for i in s:
    arr.remove(i)
    if i not in arr:
        print(i)
        break
