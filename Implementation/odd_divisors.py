for _ in range(int(input())):
    n, m = map(int, input().split())
    out = 0
    if n % 2 == 0:
        k = n//2
        out += k**2 + (k*(k+1))//2
        i = 1
        while(1):
            z = 2**i
            if z<= n:
                out -= z
                out += 1
                i += 1
            else:
                break
    else:
        k = n//2
        out += (k+1)**2 + (k*(k+1))//2
        i = 1
        while(1):
            z = 2**i
            if z<= n:
                out -= z
                out += 1
                i += 1
            else:
                break

    print(int(out%m))