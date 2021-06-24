'''
You are given an array of numbers  which contains positive as well as negative numbers . 
The cost of the array can be defined as C(X) = |A(0) + T(0)| + |........ 
where T is the transfer array which contains N zeros initially.

You need to minimize this cost . 
You can transfer value from one array element to another 
if and only if the distance between them is at most K.

Also, transfer value can't be transferred further.
'''

def Solve (k, arr):
    sum1=0
    counter=0
    m=k

    for i in arr: 
        if(i>=0):
            counter+=1
            sum1+=i
            m=k
        else:
            if(counter==0):
                return abs(sum(arr)+i)
            else:
                m-=1
                if(m<0):
                    sum1+=abs(i)
                else:
                    sum1+=i

    return abs(sum1)
 
 
 
n,k = map(int, input().split())
 
arr = map(int, input().split())

print(sum(arr))
 
out_ = Solve(k, arr)
 
print(out_)