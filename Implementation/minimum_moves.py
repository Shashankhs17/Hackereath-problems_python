'''
You want to reach a destination but you decide that
you can make moves in two directions only. 
If you are at position (x,y), then you can move to (x+1,y+1) or (x+1,y). 
You must start your journey from (0,0) and your destination is (X,Y). 
Your task is to find the minimum number of moves that you 
require to reach the destination or if you cannot reach the destination.
'''

for _ in range(int(input())):
    x ,y = map(int, input().split())
    if x>0 and y>0:
        if x>=y:
            print(x)
        else:
            print("-1")
    else:
        print("-1")