'''
A string is said to be complete if it contains all 
the characters from a to z. Given a string, 
check if it complete or not.
'''

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

match = "abcdefghijklmnopqrstuvwxyz"

n = int(input())
while n:
    string = ""
    s = input()
    s = Convert(s)
    s = set(s)
    s = sorted(s)
    string = "".join(s)
    if string == match:
        print("YES")
    else:
        print("NO")
    n -= 1