'''
You are given a number n.

A supernatural number is a number whose 
product of digits is equal to n, and in this number there is no digit 1.

Count the number of supernatural numbers for a given n.
'''
n = int(input())
flag = 1

count = 0

for i in range(2,1000000):
    pro = 1
    if '1' not in str(i) and '0' not in str(i):
        for j in range(len(str(i))):
            pro *= int(str(i)[j])
    if pro == n:
        count += 1
print(count)



# The following method is manual method: Calculating the answer and storing them in a list 

# out = [0, 1, 1, 2, 1, 3, 1, 4, 2, 2, 0, 7, 0, 2, 2, 7, 0, 7, 0, 5, 2, 0, 0, 17, 1, 0, 3, 5, 0, 8, 0, 13, 0, 0, 2, 21, 0, 0, 0, 12, 0, 8, 0, 0, 5, 0, 0, 38, 1, 3, 0, 0, 0, 15, 0, 12, 0, 0, 0, 24, 0, 0, 5, 24, 0, 0, 0, 0, 0, 6, 0, 58, 0, 0, 3, 0, 0, 0, 0, 26, 5, 0, 0, 24, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0, 82, 0, 3, 0, 9]
# n = int(input())
# print(out[n-1])