'''
You are given a positive integer n. 
The beauty factor of a number is the sum of 
digits obtained till the obtained sum is a single digit.

Example:

Beauty factor of 1987 = 1+9+8+7 = 25 = 2+5 = 7
Beauty factor of 10 = 1+0 = 1
You are given a beauty factor, b. 
Your task is to find a minimum number (n) of length k whose beauty factor is b.

Here, the length of a number is defined as the number of digits a number has. 
'''
def max_sum(digit):
    return (45 - ((9-digit)*((9-digit) + 1))//2)

def min_sum(digit):
    return (digit*(digit+1))//2

def digit_sum(num):
    s = 0
    while num:
        s += num%10
        num //= 10 
        if num == 0 and s>9:
            num = s
            s = 0
    return s

b, k = map(int, input().split())

out = []
flag = 1
pos = 0
b_ = b

if k == 1:
    print(b)
    pos = 1
else:
    while flag:
        if b>=min_sum(k):
            if k == 2:
                b = 10 + b-1
                print(b)
                pos = 1
                flag = 0
            else:
                flag = 0
                for i in range(k):
                    for j in range(1, 10):
                        if not out.count(j):
                            if b-j <= max_sum(k - 1 - i):
                                out.append(j)
                                b -= j
                                break
                if len(out) == k:
                    for item in out:
                        print(item, end="")
        else:
            flag = 0
            for i in range(b+1,100):
                if digit_sum(i) == b_:
                    b = i
                    flag = 1
                    break

if len(out)!=k:
    if not pos:
        print("-1")