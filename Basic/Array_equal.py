'''
Python3 implementation to find the minimum number of steps to equalise the 
elements of array A by subtracting the corresponding element from array B
'''

ar1 = []
ar2 = []

# Function to find the minimum steps
def minimumSteps(ar1, ar2, n):
	
	# Counter to store the steps
	ans = 0
	
	# Flag to check that
	# array is converted
	flag = True
	
	# Loop until the minimum of the
	# array is greater than -1
	while min(ar1)>-1:
		a = min(ar1)
		
		# Loop to convert the array
		# elements by substraction
		for i in range(n):
			if ar1[i]>a:
				ar1[i]-= ar2[i]
				ans+= 1
				
		# If the array is converted
		if len(set(ar1))== 1:
			flag = False
			print("Steps =",ans)
			break
	if flag:
		print("Steps = -1 ->>> Not possible to convert")

n = int(input())
arr = input()  
ar1 = list(map(int,arr.split(' ')))
arr = input()  
ar2 = list(map(int,arr.split(' ')))
minimumSteps(ar1,ar2,n)