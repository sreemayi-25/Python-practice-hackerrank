# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m,d,y=[int(x) for x in input().split(" ")]
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY","SUNDAY"]
print(days[calendar.weekday(y, m, d)])
