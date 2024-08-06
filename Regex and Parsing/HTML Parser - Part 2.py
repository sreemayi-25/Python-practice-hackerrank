# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class Parsing(HTMLParser):
    def handle_comment(self,data):
        if "\n" in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
    def handle_data(Self,data):
        if "\n" not in data:
            print(">>> Data")
            print(data)
ip=""
for i in range(int(input())):
    ip+=input().rstrip()
    ip+="\n"
par=Parsing()
par.feed(ip)
