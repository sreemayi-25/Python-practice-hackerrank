# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    for res in re.findall(r"(?<=[\D])#[0-9a-fA-F]{3,6}", input()):
        print(res) 
