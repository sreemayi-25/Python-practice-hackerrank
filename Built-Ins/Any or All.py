# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[int(x) for x in input().split(" ")]
if all(x>0 for x in l) and any(x==int(str(x)[::-1]) for x in l):
    print("True")
else:
    print("False")
      
