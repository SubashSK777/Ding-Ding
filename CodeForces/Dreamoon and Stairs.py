n, m = map(int, input().split())

if n > m and n % m == 0:
    print((n // m) + 1)
else:
    print(-1)