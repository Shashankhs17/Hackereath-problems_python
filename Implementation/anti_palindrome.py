'''
You are given a string S containing only lowercase alphabets. 
You can swap two adjacent characters any number of times (including 0).

A string is called anti-palindrome if it is not a palindrome. 
If it is possible to make a string anti-palindrome, 
then find the lexicographically smallest anti-palindrome. Otherwise, print -1.
'''
# from collections import Counter as counter                // Long method but works

# def check(lis):
#     pos = 0
#     l = len(lis)
#     c = counter(lis)
#     set_lis = set(lis)
#     for item in set_lis:
#         if c.get(item) %2 == 0:
#             pos += c.get(item)
#     if l%2 == 0:
#         if pos == l:
#             return 1
#         else:
#             return 0
#     else:
#         if len(set_lis)==1:
#             return 1
#         else:
#             if pos == l - 1:
#                 return 1
#             else:
#                 return 0

# for _ in range(int(input())):
#     s = input()
#     lis = []
#     lis[:0] = s
#     pos = check(lis)
#     if not pos:
#         s = ''.join(sorted(s))
#         print(s)
#     else:
#         print("-1")


for _ in range(int(input())):
    s = input()
    if s==s[::-1]:
        print("-1")
    else:
        print("".join(sorted(s)))