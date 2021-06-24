from collections import Counter as counter

n = int(input())
m = int(input())
r = input()

count = counter(r)
g = count.get("G")
c = count.get("C")
if g==None:
    g = 0
if c==None:
    c = 0

max = 0
max_out = 0
for i in range(n):
    l = int(input())
    s = input()
    s_count = counter(s)
    s_g = s_count.get("G")
    s_c = s_count.get("C")
    if s_c==None:
        s_c = 0
    if s_g==None:
        s_g = 0
    out = s_g*c + s_c*g
    if out>max_out:
        max_out = out
        max = i+1
print(max)
