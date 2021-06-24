from collections import Counter as counter
# lis = ['a', 'b', 'a','b','c']
lis = ['p','p','p']

pos = 0
l = len(lis)
print(l)
c = counter(lis)
set_lis = set(lis)
for item in set_lis:
    if c.get(item) %2 == 0:
        pos += c.get(item)
# l = len(set_lis)
print(l)
print(pos)
if l%2 == 0:
    if pos == l:
        print("even and palindrome")
    else:
        print("even and not palindrome")
else:
    if len(set_lis)==1:
        print("odd and palindrome")
    else:
        if pos == l or pos == l-1:
            print("odd and palindrome")
        else:
            print("odd and not palindrome")

print(lis, set_lis)
