def cube(n):
    sum = 0
    while n:
        sum += (n % 10)
        n //= 10
    sum = sum**3
    return sum

# def cube(n):
#     if n == 0:
#         return 0
#     return (n % 10 + cube(int(n / 10)))
        
out = []
test = int(input("Enter number of test cases: "))

while test:
    n, k = map(int, input("Enter value of N and K respectively: ").split())
    while k:
        sum = cube(n)**3
        n = sum
        k -= 1
    out.append(sum)
    test -= 1

for item in out:
    print(item)
