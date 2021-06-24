'''
HackerMan has brought a new drawing book for his child, 
which consists only of geometric shapes. 
Its consists of lessons where the child has to make 
drawings using the geometric shapes. 
The first lesson is based on how to use squares to build different objects.

You are task is to help HackerMan in teaching one part of this lesson. 
You have to help him in determining, given S number of squares, 
how many distinct rectangles you can build out of that.

Two rectangles are considered different if none of them 
can be rotated and moved to obtain the second one. 
During rectangle construction, the child can neither 
deform the squares nor put any squares upon any other ones.
'''


test = int(input("Enter number of test cases: "))

while test:
    rect = 0 
    squa = int(input("Enter number of squares: "))
    i = 1
    j = 0
    while 1:
        if squa//i > j:
            rect += squa//i - j
            i += 1
            j += 1
        else:
            break
    test -= 1
    print(f"Number of squares that can be formed with {squa} squares is : {rect}")