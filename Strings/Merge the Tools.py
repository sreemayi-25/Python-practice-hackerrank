def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        u=set()
        for j in range(i,i+k):
            if string[j] not in u:
                u.add(string[j]) 
                print(string[j],end="")
        print()
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
