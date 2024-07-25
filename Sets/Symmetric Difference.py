# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
arr1=set(map(int, input().split(" ")))
n=int(input())
arr2=set(map(int, input().split(" ")))
a=arr1.symmetric_difference(arr2)
b=sorted(a)
for i in b:
    print(i)
