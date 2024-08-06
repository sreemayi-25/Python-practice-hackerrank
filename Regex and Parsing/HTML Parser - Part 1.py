# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class Parsing(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(f"Start :",tag)
        for att,val in attrs:
            print(f"-> {att} > {val}")       
    def handle_endtag(self,tag):
        print(f"End   :",tag)
    def handle_startendtag(self,tag,attrs):
        print(f"Empty :",tag)
        for att,val in attrs:
            print(f"-> {att} > {val}")
ip=Parsing()
n=int(input())
ip.feed("".join(input() for i in range(n)))
