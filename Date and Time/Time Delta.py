from datetime import datetime 
# Complete the time_delta function below.
t=int(input())
for i in range(t):
    t1=input()
    t2=input()
    d1=datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    d2=datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    print(int(abs(d1-d2).total_seconds()))
