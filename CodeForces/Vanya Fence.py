n, h = map(int, input().split())

w = 0

arr = list(map(int, input().split()))

for i in arr:
    if i > h:
        w += 2
    else:
        w += 1

print(w)