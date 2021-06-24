'''
You are given an integer array . 
Your task is to calculate the sum of 
absolute difference of indices of 
first and last occurrence for every 
integer that is present in array .
'''


for _ in range(int(input())):
    n=int(input())
    k=list(map(int,input().split()))
    dic={}
    total=0
    for i in range(len(k)):
        if k[i] in dic:
            total+=i-dic[k[i]]
            dic[k[i]]=i
        else:
            dic[k[i]]=i
    print(total)

# for _ in range(int(input())):                             #METHOD 2 - Time limit exceeds
#     n = int(input())
#     a = list(map(int, input().split()))
#     a_rev = a[::-1]
#     a_set = set(a)
#     sum = 0
#     for item in a_set:
#         i = a.index(item)
#         j = n - 1 - a_rev.index(item)
#         sum += abs(i - j)
#     print(sum)