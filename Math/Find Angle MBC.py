# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import degrees,atan
ab=float(input())
bc=float(input())
mbc=round(degrees(atan(ab/bc)))
print(f"{mbc}{chr(176)}")
