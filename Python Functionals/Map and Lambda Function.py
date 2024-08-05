cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a=0
    b=1
    c=1
    l=[]
    for i in range(n):
        l.append(a)
        a=b
        b=c
        c=a+b
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
