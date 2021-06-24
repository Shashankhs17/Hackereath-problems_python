'''
You are given a table with n rows and m columns. 
Each cell is colored with white or black. 
Considering the shapes created by black cells, 
what is the maximum border of these shapes?

A shape is a set of connected cells. 
Two cells are connected if they share an edge. 
Note that no shape has a hole in it.

Input format:

-> The first line contains t denoting the number of test cases.
-> The first line of each test case contains integers n, m denoting 
   the number of rows and columns of the matrix. 
   Here, '#' represents a black cell and '.' represents a white cell. 
-> Each of the next n lines contains m integers.
'''

t = int(input())
for i in range(t): 
    n,m = list(map(int,input().split()))
    ans = 0
    arr = []
    for k in range(n):
        a=input()
        count_black = a.count('#')
        if count_black != 0:
            index_shape = a.find("#"*count_black)
            arr.append([a,1,(index_shape,count_black+index_shape-1),count_black])
        else:
            index_shape = -1
            arr.append([a,0])
    max_border = 0
    border = 0
    left_border = 0
    right_border = 0
    h_border = 0
    for k in range(n):
        if border == 0:
            if arr[k][1] == 1:
                h_border = arr[k][3]
                left_border = 1
                right_border = 1
                border = arr[k][3]
        else:
            if arr[k][1] == 1:
                range_current = arr[k][2]
                range_previous = arr[k-1][2]
                x1=range_previous[0]
                y1=range_previous[1]
                x2=range_current[0]
                y2=range_current[1]
                if x1<x2:
                    if y1==y2:
                        border = max(left_border,border)
                        h_border=max(h_border,abs(x2-x1))
                        right_border+=1
                        left_border=1
                    elif y1>y2:
                        border=max(left_border,right_border,border)
                        h_border=max(h_border,abs(x2-x1),abs(y1-y2))
                        left_border=1
                        right_border=1
                    else:
                        if x2>y1:
                            border=max(border,h_border,right_border,left_border,abs(y1-x1+1))
                            if border > max_border:
                                max_border = border
                            border = 1
                            left_border = 1
                            right_border = 1
                            h_border = abs(y2-x2+1)
                        else:
                            border=max(border,left_border,right_border)
                            h_border=max(h_border,abs(x2-x1),abs(y2-y1))
                elif x1>x2:
                    if y1==y2:
                        border=max(left_border,border)
                        h_border=max(h_border,abs(x1-x2))
                        left_border=1
                        right_border+=1
                    elif y1>y2:
                        if x1>y2:
                            border=max(border,right_border,h_border,left_border,abs(y1-x1+1))
                            if border > max_border:
                                max_border = border
                            border = 1
                            left_border = 1
                            right_border = 1
                            h_border = abs(y2-x2+1)
                        else:
                            border=max(border,right_border,left_border)
                            right_border=1
                            left_border=1
                            h_border=max(h_border,abs(x1-x2),abs(y1-y2))
                    else:
                        border=max(border,left_border,right_border)
                        left_border=1
                        right_border=1
                        h_border=max(h_border,abs(x1-x2),abs(y2-y1))
                else:
                    if y1==y2:
                        left_border+=1
                        right_border+=1
                    elif y1>y2:
                        border=max(border,right_border)
                        h_border=max(h_border,abs(y1-y2))
                        left_border+=1
                        right_border=1
                    else:
                        border=max(border,right_border)
                        right_border=1
                        left_border+=1
                        h_border=max(h_border,abs(y2-y1))
            else:
                max_border=max(max_border,h_border,right_border,left_border,border,arr[k-1][2][1]-arr[k-1][2][0]+1)
                border = 0
                left_border = 0
                right_border = 0
                h_border = 0
    print(max(max_border,h_border,right_border,left_border,border))