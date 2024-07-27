# Enter your code here. Read input from STDIN. Print output to STDOUT
no=int(input())
arr1=set(map(int, input().split(" ")))
n=int(input())
for i in range(n):
    n=list(input().split(" "))
    if n[0]=="intersection_update":
        arr2=set(map(int, input().split(" ")))
        arr1.intersection_update(arr2)
    elif n[0]=="update":
        arr2=set(map(int, input().split(" ")))
        arr1.update(arr2)
    elif n[0]=="symmetric_difference_update":
        arr2=set(map(int, input().split(" ")))
        arr1.symmetric_difference_update(arr2)
    elif n[0]=="difference_update":
        arr2=set(map(int, input().split(" ")))
        arr1.difference_update(arr2)
print(sum(arr1))
    
