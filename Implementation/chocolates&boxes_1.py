test = int(input("Enter number of test cases: "))

while test:
    n = int(input("Enter number of boxes: "))
    data = list(map(int, input("Enter number of chocolates in each box: ").split()))
    k = int(input("Enter value of k: "))
    l = len(data)
    count = 0
    for i in range(l):
        for j in range(i+1, l):
            if data[i] + data[j] == k:
                count += 1
    print(count)
    test -= 1