'''
You like the sound of rain only if the sound ranges from l to r units. 
Every cloud makes  unit of sound. Determine the minimum and the maximum 
number of clouds that can produce the sound in the provided range.
'''

for _ in range(int(input())):
    l, r, s = map(int, input().split())
    min = max = -1
    if l%s == 0:
        min = l//s 
    else:
        min = l//s + 1
    if min*s>r:
        min = -1
    max = r//s
    if max <= 0 or min == -1:
        max = -1
    print(min,max)