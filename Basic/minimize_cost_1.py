'''
You are given an array of numbers  which contains positive as well as negative numbers . 
The cost of the array can be defined as C(X) = |A(0) + T(0)| + |........ 
where T is the transfer array which contains N zeros initially.

You need to minimize this cost . 
You can transfer value from one array element to another 
if and only if the distance between them is at most K.

Also, transfer value can't be transferred further.
'''

# High runtime

n, k = map(int,input("Enter value of 'N' & 'K' respectively: ").split())

A = list(map(int,input("Enter array A elements: ").split()))

T = [0] * n
a = tuple(A)

cost = 0

i = 0
while i<n:
    if A[i]>0:
        m = i + k + 1
        if m>n:
            m = n

        j = i+1
        while j<m:
            if A[j]<0 and A[i]>0:
                if abs(A[j])>=A[i]:
                    T[i] += -1 * A[i]
                    T[j] += A[i]
                    A[j] += A[i]
                    A[i] = 0
                else:
                    T[i] += A[j]
                    T[j] += -1 * A[j]
                    A[i] += A[j]
                    A[j] += T[j]
            j += 1

    sum = abs(a[i] + T[i])
    cost += sum
    i += 1

print(int(cost))