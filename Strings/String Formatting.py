def print_formatted(n):
    # your code goes here
    l=len(bin(n)[2:])
    for i in range(1,n+1):
        b=bin(i)[2:] 
        o=oct(i)[2:]
        h=hex(i)[2:].upper()
        nn=str(i)
        print(nn.rjust(l," "),o.rjust(l," "),h.rjust(l," "),b.rjust(l," "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
