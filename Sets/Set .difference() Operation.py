# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr1=set(map(int, input().split(" ")))
m=int(input())
arr2=set(map(int, input().split(" ")))
print(len(arr1.difference(arr2)))
