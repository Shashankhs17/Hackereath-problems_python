'''
You are given an array of size N that contains integers.
Here, N is an even number. You are required to perform the following operations:

-> Divide the array of numbers in two equal halves
         Note: Here, two equal parts of a test case are created by dividing the array into two equal parts.
-> Take the first digit of the numbers that are available in the first half of the array (first 50% of the test case)
-> Take the last digit of the numbers that are available in the second half of the array (second 50% of the test case)
-> Generate a number by using the digits that have been selected in the above steps

Your task is to determine whether the newly-generated number is divisible by 11.

'''

from math import fabs

n = int(input("Enter n:"))

arr = [x for x in input("Enter the array elements: ").split(" ")]

num = []

sum_odd = sum_even = 0

for i in range(n):
    if i<n/2:
        num.append(arr[i][0])
    else:
        lenght = len(arr[i])
        num.append(arr[i][lenght-1])

for i in range(n):
    if i % 2 == 0:
        sum_odd += int(num[i])
    else:
        sum_even += int(num[i])

if fabs(sum_even - sum_odd) % 11 == 0:
    print("OUI")
else:
    print("NON")