# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
while t>0:
    n=int(input())
    arr1=set(map(int, input().split(" ")))
    m=int(input())
    arr2=set(map(int, input().split(" ")))
    print(arr1.issubset(arr2))
    t=t-1
