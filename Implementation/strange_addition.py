'''
HackerMan has a message that he has coded in form of digits, 
which means that the message contains only numbers and nothing else. 
He is fearful that the enemy may get their hands on the secret message and may decode it. 
HackerMan already knows the message by heart and he can simply destroy it.

But he wants to keep it incase its needed in a worse situation. 
He wants to further encode the message in such a format which is not completely reversible. 
This way if enemies gets hold of the message they will not be completely able to decode the message.

Since the message consists only of number he decides to flip the numbers. 
The first digit becomes last and vice versa. For example, if there is 3769 in the code, it becomes 9673 now. 
All the leading zeros are omitted e.g. 15900 gives 951. 
So this way the encoding can not completely be deciphered and has some loss of information.

HackerMan is further thinking of complicating the process and he needs your help. 
He decides to add the two flipped numbers and print the result in the encoded (flipped) form. 
There is one problem in this method though. For example, 134 could be 431, 4310 or 43100 before reversing. 
Hence the method ensures that no zeros were lost, that is it can be assumed that the original number was 431.
'''

def flip(num):
    while num%10 == 0:
        num = num//10
    num = str(num)
    num = num[::-1]
    num = int(num)
    return num

test = int(input("Enter number of test cases: "))

while test:
    a, b = map(int, input("Enter the two numbers:").split())
    a = flip(a)
    b = flip(b)
    out = a + b
    out = flip(out)
    print(out)
    test -= 1