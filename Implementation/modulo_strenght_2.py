'''
Alice is the teacher of a class having N students, 
where each student is having some personality value, 
given in the form of an array A. 
Here A(i) denotes the personality value of i'th student. 
Alice has special integer K with her. 
Student i is a friend of Student j, if and only if (A[i] % k = A[j] % k). 
Each student's strength is equal to the number of friends he/she has. 
Alice needs to calculate the sum of the strength of all the students in the class. 
Help Alice for the same.
'''

d={}
k = int(input().split()[1])
l = [int(i) for i in input().split()]
for i in l:
     try: d[i%k] += 1
     except: d[i%k] = 1
print(sum(d[i] * (d[i]-1) for i in d))