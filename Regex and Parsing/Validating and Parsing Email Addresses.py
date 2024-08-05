import re
import email.utils
n=int(input())
for i in range(n):
  a=(email.utils.parseaddr(input()))
  ptr=(r"^[a-z]+.*@[a-z]+\.[a-z]{1,3}$")
  if re.search(ptr,a[1]):
    print(email.utils.formataddr(a))
