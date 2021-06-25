'''
You are given a polygon of N sides with vertices numbered from 1-N. 
Now, exactly 2 vertices of the polygons are colored black and remaining are colored white. 
You are required to find the number of triangles denoted by A such that:

1. The triangle is formed by joining only the white-colored vertices of the polygon.
2. The triangle shares at least one side with the polygon.
'''

for _ in range(int(input())):
    n, b1, b2 = map(int, input().split())
    x = 0
    minus = 0
    out = 0
    if n - 2 > 3:
        if b1>b2:
            b1, b2 = b2,b1

        diff = (b2 - b1 - 1)

        if diff>=2:
            x = (diff - 1)
            minus = (diff - 2)
            out += x*(n-4) - minus
        
        diff = (b1 - 1) + (n - b2)

        if diff>=2:
            x = (diff - 1)
            minus = (diff - 2)
            out += x*(n-4) - minus

    else:
        out = 1
    print(out)