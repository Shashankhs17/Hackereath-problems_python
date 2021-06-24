'''
You are provided an array A of size N that contains non-negative integers. 
Your task is to determine whether the number that is formed by 
selecting the last digit of all the N numbers is divisible by 10.
'''

n = int(input())
flag = 0

arr = input()  
ar1 = list(map(int,arr.split(' ')))

for i in range(n):
    if i == n-1:
        if ar1[i] % 10 == 0:
            flag = 1
        else:
            flag = 0

if flag == 1:
    print("Yes")
else:
    print("No")