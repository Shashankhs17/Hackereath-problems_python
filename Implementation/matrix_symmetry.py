for _ in range(int(input())):
    n = int(input())
    matrix = []
    for i in range(n):
        r = []
        r = list(map(str, input()))
        matrix.append(r)

    h = v = 0

    k = n - 1
    for j in range(n//2):
        # k = n - 1
        for i in range(n):
            if matrix[j][i] == matrix[k][i]:
                h += 1
            else:
                break
        k -= 1

    k = n - 1
    for j in range(n//2):
        # k = n - 1
        for i in range(n):
            if matrix[i][j] == matrix[i][k]:
                v += 1
            else:
                break
        k -= 1

    z = n*(n//2)

    print(h,v)

    if h == z and v == z:
        print("BOTH")
    elif h == z and v != z:
        print("HORIZONTAL")
    elif h != z and v == z:
        print("VERTICAL")
    else:
        print("NO")