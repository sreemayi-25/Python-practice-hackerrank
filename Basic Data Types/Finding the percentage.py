if __name__ == '__main__':
    n=int(input())
    marks = {}
    for i in range(n):
        data= input().split()
        name=data[0]
        scores = list(map(float, data[1:]))
        marks[name]=scores
    name = input()
    if name in marks.keys():
        avg=sum(marks[name])/3
        print("%.2f" %avg)
        
