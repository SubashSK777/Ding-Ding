n = int(input())
arr = list(map(int, input().split()))   # 3 2 5 1 7

l = len(arr)

res = 0

for i in range(1, l):
    if arr[i - 1] > arr[i]:
        dif = arr[i - 1] - arr[i]
        res += dif
        arr[i] += dif

print(res)


