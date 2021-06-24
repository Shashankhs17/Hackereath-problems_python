'''
While playing a mental math game, 
you realize that the number k is mathematically beautiful.

You then realize that the number x can be 
mathematically beautiful if it is represented as a 
sum of a sequence where each element is a 
power of k and all the numbers in the sequence are different.

Task

Your task is to determine whether the number is mathematically beautiful.
'''


for _ in range(int(input())):
    n, k = map(int, input().split())
    flag = 0
    while(n >= k):
        if n % k == 0 or n % k == 1:
            n //= k
            flag = 1
        else:
            flag = 0
            break
    if flag:
        print("YES")
    else:
        print("NO")