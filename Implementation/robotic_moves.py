'''
A robot's initial position is (0,0) and it can only move along X-axis. 
It has N moves to make and in each move, it will select one of the following options:

    -> Go to (x-1,0) from (x,0)
    -> Go to (x+1,0) from (x,0)
    -> Remain at its current position

Your task is to calculate sum(abs(x) + abs(y)) for all reachable (x, y).
'''

for _ in range(int(input())):
    n = int(input())
    print(n*(n+1))