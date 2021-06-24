'''
Implement the recursive function given by the following rules and print the last 3 digits:

F(x, y) = 
{
y + 1 when x = 0,
F(x - 1, 1) when x > 0 and y = 0,
F(x - 1, F(x, y - 1)) when x > 0 and y > 0
}
'''

from functools import lru_cache
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(10**8)
print(sys.getrecursionlimit())

@lru_cache(maxsize=None)
def f(x,y):
    x %= 1000
    y %= 1000
    if x == 0:
        return y+1
    elif x>0 and y == 0:
        return f(x-1 , 1)
    elif x>0 and y>0:
        return f(x-1, f(x, y-1))
    else:
        return -1

x, y = map(int, input().split())
out = f(x, y)
out = str(out)
print(out.zfill(3))