if __name__ == '__main__':
    lst=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        l=[]
        l.append(name)
        l.append(score)
        lst.append(l)  
    scores=set()
    lst.sort()
    for i in range(n):
        scores.add(lst[i][1])
    scores.remove(min(scores))
    sec_min=min(scores)
    #print(sec_min)
    for i in range(n):
        if lst[i][1]==sec_min:
            print(lst[i][0])     
