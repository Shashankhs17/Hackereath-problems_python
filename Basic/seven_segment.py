'''
Alice got a number written in seven segment format where each segment was creatted used a matchstick.

Example: If Alice gets a number 123 so basically Alice used 12 matchsticks for this number.

Alice is wondering what is the numerically largest value that she can generate by using at most 
the matchsticks that she currently possess.Help Alice out by telling her that number.
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
    
# def check_sticks(sum_sticks):
#     num_max = 0
#     if sum_sticks == 2:
#         num_max = 0
#     elif sum_sticks == 3:
#         num_max = 7
#     elif sum_sticks == 4:
#         num_max = 4
#     elif sum_sticks == 5:
#         num_max = 5
#     elif sum_sticks == 6:
#         num_max = 6
#     elif sum_sticks == 7:
#         num_max = 8
#     else:
#         num_max = 0

test = int(input("Enter number of tests you want to perform:"))
num_array = []
for i in range(test):
    num = input("Enter the number:")
    num_array.append(num)
print(num_array)

j = 0

while test:
    num_max_array = []
    number = str(num_array[j])
    sum_sticks = 0
    for i in range(len(number)):
        sum_sticks += check_num(int(number[i]))
    print(sum_sticks)
    if sum_sticks >= 2:
        if sum_sticks % 2 == 0:
            digits = (sum_sticks / 2) 
            while digits > 0:
                num_max_array.append("1")
                digits -= 1
        else:
            digits = (sum_sticks // 2) 
            num_max_array.append("7")
            digits -= 1
            while digits>0:
                num_max_array.append("1")
                digits -= 1
    else:
        print("Not possible")
    
    test -= 1 
    j += 1
    for item in num_max_array:
        print(item, end="")
    print("\n",end="")