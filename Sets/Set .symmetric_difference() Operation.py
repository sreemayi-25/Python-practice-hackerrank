# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
arr1=set(map(int, input().split(" ")))
n=int(input())
arr2=set(map(int, input().split(" ")))
print(len(arr1.symmetric_difference(arr2)))
