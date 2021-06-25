# from functools import lru_cache
# from sys import setrecursionlimit
# setrecursionlimit(1000000)

# @lru_cache(maxsize=None)
# def f(n):
#     if n == 1:
#         return 1
#     else:
#         if n % 2 != 0:
#             return n + f(n-1)
#         else:
#             while n != 0:
#                 n //= 2
#                 if n%2 != 0:
#                     break
#             return n + f(n-1)


for _ in range(int(input())):
    n, m = map(int, input().split())
    out = 0
    if n % 2 == 0:
        k = n//2
        out += k**2 + (k*(k+1))//2
        i = 1
        while(1):
            z = 2**i
            if z<= n:
                out -= z
                out += 1
                i += 1
            else:
                break
    else:
        k = n//2
        out += (k+1)**2 + (k*(k+1))//2
        i = 1
        while(1):
            z = 2**i
            if z<= n:
                out -= z
                out += 1
                i += 1
            else:
                break

    # for i in range(1,n+1):
    #     if i%2 == 0:
    #         while i!=0:
    #             i //= 2
    #             if i%2 != 0:
    #                 out += i
    #                 break
    #     else:
    #         out += i

    # out = f(n)

    print(int(out%m))