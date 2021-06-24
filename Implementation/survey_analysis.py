'''
WebEngage empowers companies to collect feedback and 
gather insights from visitors using survey and notifications.

An e-commerce company used the WebEngage customer engagement tool 
to ask visitors if they want to buy the selected products at discounted prices. 
If the visitor said 'Yes', the product was delivered to the customer at the discounted price. 
They collected the response for a whole week from Monday to Sunday. 
Now they want to analyse which day most of the people said 'Yes' compared to other days. 
For this, they want to calculate the standard deviation of the 'Yes' count on each day. 
Using the standard deviation, we have a standard way of knowing 
which day was extra good, which day was extra bad, and which day was just plain normal in terms of business.

Input format:

The input contains 7 lines, depicting Monday to Sunday. 
Each line contains a string of 1 & 0. 1 means the visitor said 'Yes', and 0 means the visitor said 'No'.


'''

from math import sqrt

out = []

for i in range(7):
    count = 0
    data = input("Enter the string containing the data of the survey: ")
    for i in range(len(data)):
        if data[i] == "1":
            count += 1
    out.append(count)

mean = sum(out)/7
for i in range(7):
    out[i] = (out[i] - mean)**2
sd = sqrt(sum(out)/7)
print("%.4f"%sd)