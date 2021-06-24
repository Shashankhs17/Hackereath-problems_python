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
    l = len(string)
    string = string.replace('a', ' ').replace('z', ' ').split()
    for i in string:
        k = len(i)
        count += (k*(k+1))/2
    return (l * (l+1))/2 - count           
             
test = int(input("Enter number of test cases: "))

while test:
    M = input("Enter the alien message: ")
    count = substring(M)
    print(f"Number of valid substrings that can be made with the given message string is: {int(count)}")
    test -= 1