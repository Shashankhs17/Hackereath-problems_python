'''
You are given a string, which contains entirely of decimal digits (0-9). 
Each digit is made of a certain number of dashes. 
For instance 1 is made of 2 dashes, 8 is made of 7 dashes and so on.

You have to write a function that takes this string message as an input 
and returns a corresponding value in terms of a number. 
This number is the count of dashes in the string message.
'''


def check_num(num):
    sticks = 0
    if num == 0:
        sticks = 6
    elif num == 1:
        sticks = 2
    elif num == 2:
        sticks = 5
    elif num == 3:
        sticks = 5
    elif num == 4:
        sticks = 4
    elif num == 5:
        sticks = 5
    elif num == 6:
        sticks = 6
    elif num == 7:
        sticks = 3
    elif num == 8:
        sticks = 7
    elif num == 9:
        sticks = 6
    else:
        sticks = 0
    
    return sticks

inp = input("Enter the string of numbers: ")
sum = 0
for i in range(len(inp)):
    sum += check_num((int(inp[i])))
print(sum)