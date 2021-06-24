'''
You have been given a positive integer N.
You need to find and print the Factorial of this number.
'''

n = int(input("Enter number to find it's factorial:"))

fact = 1

i = n
while i>0:
    fact *= i
    i -= 1
print(f"Factorial of {n} = {fact}")