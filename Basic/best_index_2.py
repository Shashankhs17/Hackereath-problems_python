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

def bestIndex(n, arr):
    i, j, k = 0, 2, 1
    while j + k <= n:
        k += j
        j += 1
 
    prefix_sum = [0] * (n + 1)
    t = 1
 
    while t < n + 1:
        prefix_sum[t] = prefix_sum[t-1] + arr[t-1]
        t += 1

    ans = -10 ** 7
 
    while i < n:
        ans = max(ans, prefix_sum[k+i] - prefix_sum[i])
        i += 1
        if i + k > n:
            j -= 1 
            k -= j

    return ans

n = int(input("Enter n: "))
arr = list(map(int,input("Enter array elements: ").split()))
print(bestIndex(n,arr))