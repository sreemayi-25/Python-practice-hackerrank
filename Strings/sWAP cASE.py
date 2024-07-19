def swap_case(s):
    swap=""
    for i in s:
        if i.isupper():
            swap+=i.lower()
        else:
            swap+=i.upper()
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
