'''
You have been given a String S. 
You need to find and print whether this string is a palindrome or not. 
If yes, print "YES" (without quotes), else print "NO" (without quotes).

'''

string = input("Enter the string:")
lenght = len(string)
flag = 0

i = 0
while i<lenght/2:
    if string[i] == string[lenght - 1]:
        flag = 1
    else:
        flag = 0
        break
    
    i += 1
    lenght -= 1

if flag == 1:
    print("YES")
else:
    print("NO")