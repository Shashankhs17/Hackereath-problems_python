'''
Arpasland has surrounded by attackers. A truck enters the city. 
The driver claims the load is food and medicine from Iranians. 
Ali is one of the soldiers in Arpasland. 
He doubts about the truck, maybe it's from the siege. 
He knows that a tag is valid if the sum of every 
two consecutive digits of it is even and its letter is not a vowel. 
Determine if the tag of the truck is valid or not.

We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.

Input Format

The first line contains a string of length 9. 
The format is "DDXDDD-DD", where D stands for a digit (non zero) and X is an uppercase english letter.
'''


import re
from sys import exit

str = input("Enter the tag number: ")

matched = re.match("[0-9][0-9][A-Z][0-9][0-9][0-9][-][0-9][0-9]", str)
is_match = bool(matched)
if is_match:
    pass
else:
    print("invalid")
    exit()


if str[2] == 'A' or str[2] == 'E' or str[2] == 'I' or str[2] == 'O' or str[2] == 'U' or str[2] == 'Y':
    print("invalid")
    exit()
else:
    pass

for i in range(len(str)-1):
    if str[i].isdigit() and str[i+1].isdigit():
        n = int(str[i])+int(str[i+1])
        if n % 2 == 0:
            pass
        else:
            print("invalid")
            exit()

print("valid")