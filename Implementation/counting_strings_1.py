'''
Alice got a message M. It is in an alien language. 
A string in an alien language is said to be valid 
if it contains the letter a or z. 
Alice decided to count the number of valid 
substrings of the message M. Help him to do this. 
Two substrings are different if it occurs at 
different positions in the message.
'''

def substring(string):
    count = 0
    k = 1
    while 1:
        for i in range(len(string)):
            j = i + k
            if j <= len(string):
                try:
                    sub = string[i:j]
                    print(sub)
                    if "a" in sub or "z" in sub:
                        count += 1
                except:
                    pass
        k += 1
        if k > len(string):
            break
    return count           

test = int(input("Enter number of test cases: "))

while test:
    M = input("Enter the alien message: ")
    count = substring(M)
    print(f"Number of valid substrings that can be made with the given message string is: {int(count)}")
    test -= 1
