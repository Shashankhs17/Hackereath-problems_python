'''

from math import gcd

def SpecialSum(N):
    ret=0
    i = 1
    while i <= N:
        if N % i == 0:
            j = 1
            while j<=i:
                if gcd(i, j) == 1:
                    ret += 1
                j += 1
        i += 1
    return ret

for _ in range(int(input())):
    n = int(input())
    out = SpecialSum(n)
    print(out) 

'''

for _ in range(int(input())):
    n = int(input())
    print(n) 