'''
Its Diwali time and there are LED series lights everywhere. 
Little Roy got curious about how LED lights work.

He noticed that in one single LED Bulb 
there are 3 LED lights, namely Red, Green and Blue.

State of the bulb at any moment is 
the sum of Red, Green and Blue LED light.

Bulb works as follows:

R = R
G = G
B = B
R + G + B = WHITE
--------- = BLACK
R + G + - = YELLOW
R + - + B = MAGENTA
- + G + B = CYAN 

Roy took out all the LEDs and found that 
Red LED stays ON for R seconds, 
Green LED stays ON for G seconds and 
Blue LED stays ON for B seconds. 

Similarly they stay OFF for same respective R, G, B number of seconds. 
(Initially all the LEDs are OFF)

Roy has one query for you, given the total number of seconds T, 
find the number of seconds Red, Green, Blue, Yellow, Cyan, Magenta, White, Black(no light) lights are visible.
'''

t, r, g, b = map(int, input("Enter value of T, R, G & B respectively: ").split())

r_ = g_ = b_ = y_ = c_ = m_ = w_ = b__ = 0
k = l = m = 1

x = y = z = 0

for i in range(1, t+1):
    if i <= k*r:
        x = 0
    elif i>k*r and i<(k+1)*r:
        x = 1
    else:
        x = 1
        k += 2
    
    if i <= l*g:
        y = 0
    elif i>l*g and i<(l+1)*g:
        y = 1
    else:
        y = 1
        l += 2

    if i <= m*b:
        z = 0
    elif i>m*b and i<(m+1)*b:
        z = 1
    else:
        z = 1
        m += 2
    if x and y and z:
        w_ += 1
    elif x and y and not z:
        y_ += 1
    elif x and not y and z:
        m_ += 1
    elif not x and y and z:
        c_ += 1
    elif x and not y and not z:
        r_ += 1
    elif not x and y and not z:
        g_ += 1
    elif not x and not y and z:
        b_ += 1
    else:
        b__ += 1

print(r_, g_, b_, y_, c_, m_, w_, b__)