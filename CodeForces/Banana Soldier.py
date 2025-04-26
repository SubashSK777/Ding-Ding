k, n, w = map(int, input().split())

res = ((w * (w + 1))// 2) * k - n

print(res if res > 0 else 0)
