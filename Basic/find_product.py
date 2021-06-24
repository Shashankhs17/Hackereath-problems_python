'''
You have been given an array A of size N consisting of positive integers. 
You need to find and print the product of all the number in this array modulus 10^9 +7.
'''
n = int(input("Enter n: "))

arr = list(map(int,input("Enter array elements: ").split()))

ans = 1

i = 0
while i<n:
    ans = (ans * arr[i]) % (10**9 + 7)
    i += 1

print(ans)