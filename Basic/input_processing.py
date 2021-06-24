'''
Your program is to use the brute-force approach in order to 
find the Answer to Life, the Universe, and Everything. 
More precisely... rewrite small numbers from input to output. 
Stop processing input after reading in the number 42. 
All numbers at input are integers of one or two digits.
'''

flag = 1
out = []
while flag:
    num = int(input("Enter the number:"))
    if num != 42:
        out.append(num)
    else:
        flag = 0
for item in out:
    print(item)