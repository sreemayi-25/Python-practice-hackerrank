def minion_game(string):
    # your code goes here
    k=0
    s=0
    for i in range(len(string)):
        if string[i].lower() in "aeiou":
            k+=len(string[i:])
        else:
            s+=len(string[i:])
    if s>k:
        print("Stuart",s)
    elif s<k:
        print("Kevin",k)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
