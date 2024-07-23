import string
def print_rangoli(size):
    # your code goes here
    a=string.ascii_lowercase
    l=4*size-3
    lines=[]
    for i in range(size):
        s="-".join(a[size-1:size-1-i:-1]+a[size-1-i:size])
        lines.append(s.center(l,"-"))
    print("\n".join(lines+lines[-2::-1]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
