'''
You are given a number N. 
You are required to determine the value of the following function:

long long int solve(N)
{
    ans=0;
    for(i=1;i<=N;i++)
    ans+=(N/i);
    return ans;
}

All divisions are integer divisions(i.e. N/i is actually floor(N/i))
'''

def solve(n):
    x = int(pow(n,0.5))
    ans = 0
    for i in range(1,x+1):
        ans = ans + n//i
    ans = 2*ans-(x*x)
    return ans

for _ in range(int(input())):
    print(solve(int(input())))

