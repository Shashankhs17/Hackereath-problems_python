'''
It's 12 o'clock at midnight (00:00) and Simon cannot sleep! 
So he decided to stare at the clock on his wall until he falls asleep.

He saw the clock's hands and got to thinking 
'How many times they'll pass each other until I fall asleep'. 
Imagine that he fell asleep at hh:mm . 
Now, you must  figure out how many times clock's hands overlap from 00:00 to hh:mm (including 00:00 and hh:mm).
'''

h, m = map(int, input().split(":"))

count = 0
if h>=12:
    h -= 12
    count += 11

for i in range(h+1):
    h_ = i*30
    if i == h:
        k = m*6
    else: 
        k = 359
    for j in range(k+1):
        if h_ == j:
            count += 1
            print(h_,j)
        if j%12 == 0 and j != h_:
            h_ += 1

print(count)
