'''
You have been given 3 integers - l, r and k. 
Find how many numbers between l and r (both inclusive) are divisible by k. 
You do not need to print these numbers, you just have to find their count.
'''

l, r, k = map(int,input("Enter value of 'l', 'r' & 'k' respectively: ").split())
print(f"l = {l}, r = {r}, k = {k}")

count = 0
while l<r+1:
    if l % k == 0:
        count += 1
    l += 1
print(f"count = {count}")