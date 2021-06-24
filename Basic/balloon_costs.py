'''
You are conducting a contest at your college. This contest consists of two problems and N participants. 
You know the problem that a candidate will solve during the contest.
You provide a balloon to a participant after he or she solves a problem. 
There are only green and purple-colored balloons available in a market. 
Each problem must have a balloon associated with it as a prize for solving that specific problem. 
You can distribute balloons to each participant by performing the following operation:

-> Use green-colored balloons for the first problem and purple-colored balloons for the second problem
-> Use purple-colored balloons for the first problem and green-colored balloons for the second problem

You are given the cost of each balloon and problems that each participant solve. 
Your task is to print the minimum price that you have to pay while purchasing balloons.
'''
test = int(input("Enter number of test cases:"))

out = []

while test:
    sum_green = 0
    sum_purple = 0
    cost = [int(x) for x in input("Enter the cost of GREEN and PURPLE colored balloons:").split(" ")]
    n = int(input("Enter number of candidates:"))
    print("Enter the submission data:")
    for i in range(n):
        data = [int(x) for x in input().split(" ")]
        sum_green += (data[0]*cost[0]) + (data[1]*cost[1])
        sum_purple += (data[0]*cost[1]) + (data[1]*cost[0])
    out.append(min(sum_green, sum_purple))
    test -= 1

for item in out:
    print(item)