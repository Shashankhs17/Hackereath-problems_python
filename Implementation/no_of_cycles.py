'''
You are given an N-sided regular polygon. 
You have connected the center of the polygon with all the vertices, 
thus dividing the polygon into N equal parts.

Your task is to find the count of simple cycles that exist in the modified structure of the polygon.
'''

for _ in range(int(input())):
    n = int(input())
    print((n*(n-1))+1)