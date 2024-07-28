# Enter your code here. Read input from STDIN. Print output to STDOUT
s=set(map(int, input().split(" ")))
n=int(input())
res=""
for i in range(n):
    arr=set(map(int, input().split(" ")))
    if s.issuperset(arr):
        res="True"
    else:
        res="False"
        break
print(res)
