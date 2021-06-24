from math import gcd
from itertools import combinations

def FourSeven(N, base):
   n = base*10
   if(n+4<=N):
       FourSeven(N, n+4)
       if(1<=n+4):
           out.append(n+4) 
   if(n+7<=N):
       FourSeven(N, n+7)
       if(1<=n+7):
           out.append(n+7)

N = int(input())

out = []

FourSeven(N, 0)
 
comb = combinations(out,2)

count = 0

for item in comb:
    if gcd(item[0],item[1])==1:
        count += 1
print(count)
