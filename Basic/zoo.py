'''
You are required to enter a word that consists of x and y that
denote the number of Zs and Os respectively. 
The input word is considered similar to word zoo
if 2x = y.Determine if the entered word is similar to word zoo.
'''

word = input("Enter the word containing only z's and o's:")
x = 0
y = 0

for letter in word:
    if letter == 'z':
        x+=1
    elif letter == 'o':
        y+=1
    else:
        print("You have included a wrong letter in the world")

if(2*x == y):
    print("Yes")
else:
    print("No")