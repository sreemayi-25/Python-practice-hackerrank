# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr1=set(map(int, input().split(" ")))
b=int(input())
arr2=set(map(int, input().split(" ")))
res=arr1.union(arr2)
print(len(res))
