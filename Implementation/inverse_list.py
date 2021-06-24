'''
There are many ways to order a list of integers from 1 to n. 
For example, if n = 3, the list could be :[3 1 2] .

But there is a special way to create another list from the given list of integers. 
In this list, position of integer i is the i-1 th number in the given list. 
So following this rule, the given list will be written as: [2 3 1]. 
This list is called inverse list. 
Now there exists some list whose inverse list is identical. 
For example, inverse list of [1 2 3] is same as given list. 
Given a list of integers you have to determine whether the list is inverse or not.
'''

test = int(input("Enter number of test cases: "))

while test:
    flag = 0
    n = int(input("Enter value of n: "))
    out = []
    arr = list(map(int, input("Enter list elements: ").split()))
    for i in range(n):
        num = arr[i]
        index = arr[num - 1] - 1
        out.insert(index, num)
    print(out)
    for i in range(n):
        if arr[i] == out[i]:
            flag = 1
        else:
            flag = 0
            break
    if flag:
        print("inverse")
    else:
        print("not inverse")
    test -= 1
    