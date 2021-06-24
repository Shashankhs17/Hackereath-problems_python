'''
You have been given a String S consisting of uppercase and lowercase English alphabets. 
You need to change the case of each alphabet in this String. 
That is, all the uppercase letters should be converted to lowercase and 
all the lowercase letters should be converted to uppercase. 
You need to then print the resultant String to output.

'''

str = input("Enter the string:")
str_out = []

i = 0
while i<len(str):
    if str[i].isupper():
        str_out.append(str[i].lower())
    elif str[i].islower():
        str_out.append(str[i].upper())
    else:
        break

    i += 1
for item in str_out:
    print(item, end="")