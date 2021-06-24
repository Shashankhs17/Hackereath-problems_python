'''
You are given an array A of N elements. Now you need to choose the best index of this array. 
An index of the array is called best if the special sum of this index is maximum across the special sum of all the other indices.
To calculate the special sum for any index i,
you pick the first element that is A[i] and add it to your sum. 
Now you pick next two elements i.e. A[i+1] & A[i+2] and add both of them to your sum. 
Now you will pick the next 3 elements and this continues till the index for which it is possible to pick the elements. 
For example:
If our array contains 10 elements and you choose index to be 3 then your special sum is denoted by -
{A[3]} + {A[4] + A[5]} + {A[6] + A[7] + A[8]}, 
beyond this its not possible to add further elements as the index value will cross the value .

Find the best index and in the output print its corresponding special sum. 
Note that there may be more than one best indices but you need to only print the maximum special sum.
'''

# This code has bit high run time

n = int(input("Enter n: "))

arr = list(map(int,input("Enter array elements: ").split()))

special_sum = 0
sum_final = 0
i = 0

while i<n:
    a = 1
    b = i
    special_sum = 0

    while a+b <= n:
        j = b
        while j<b+a:
            special_sum += arr[j]
            j += 1
        b = b + a
        a += 1
    sum_final = max(sum_final, special_sum)
    i += 1
print(sum_final)