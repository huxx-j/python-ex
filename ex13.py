import random as r

s = set([])
l = 0
while l<6:
    num = int(r.random() * 45) + 1
    s.add(num)
    l = len(s)

print(s)
