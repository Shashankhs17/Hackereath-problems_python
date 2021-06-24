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

n, k = map(int, input("Enter the value of n and k respectively: ").split())

A = list(map(int, input("Enter personality index of each student: ").split()))

A = [A[i] % k for i in range(n)]
B = set(A)
strenght = 0
for item in B:
    strenght += A.count(item) * (A.count(item) - 1)
print(strenght) 