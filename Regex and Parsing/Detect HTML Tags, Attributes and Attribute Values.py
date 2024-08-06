# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class parsing(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        for a in attrs:
            n,val=a
            print(f"-> {n} > {val}")
ip=parsing()
n=int(input())
ip.feed("".join([input() for i in range(n)]))
    
