'''
Roy wants to change his profile picture on Facebook. 
Now Facebook has some restriction over the dimension of picture that we can upload.
Minimum dimension of the picture can be L x L, where L is the length of the side of square.

Now Roy has N photos of various dimensions.
Dimension of a photo is denoted as W x H
where W - width of the photo and H - Height of the photo

When any photo is uploaded following events may occur:

[1] If any of the width or height is less than L, user is prompted to upload another one. Print "UPLOAD ANOTHER" in this case.
[2] If width and height, both are large enough and
    (a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.
    (b) else user is prompted to crop it. Print "CROP IT" in this case.

'''

l = int(input("Enter value of L: "))
n = int(input("Enter n(Number of photos): "))
flag_array = []

i = 0
while i<n:
    flag = 0
    w, h = list(map(int,input("Enter value of 'w' & 'h' respectively: ").split()))
    if w<l or h<l:
        flag = 1
    elif w == h:
        flag = 2
    else:
        flag = 3
    flag_array.append(flag)
    i += 1

for item in flag_array:
    if item == 1:
        print("UPLOAD ANOTHER")
    elif item == 2:
        print("ACCEPTED")
    else:
        print("CROP IT")    