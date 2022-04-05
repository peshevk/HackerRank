import re

regex = r"(?:([a-zA-Z\d])(?!.*\1)){10}"
n = int(input())

for _ in range(n):
    uid = input()
    if re.match(regex, uid):
        print("Valid")
    else:
        print("Invalid")



