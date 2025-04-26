n, k = map(int, input().split())

arr = list(map(int, input().split()))

t = arr[k]

if t == 0:
    print('0')
else:
    res = 0

    for i in arr:
        if i >= t:
            res += 1

    print(res)