n = int(input())

arr = list(map(int, input().split()))

h = l = 0

for i in range(n):
    if arr[i] >= arr[h]:
        h = i
    if arr[i] <= arr[l]:
        l = i

if arr[h] == arr[0] and arr[l] == arr[-1]:
    print(0)
elif h > l:
    print(h + (n - l - 2))
elif h < l:
    print(h + (n - l - 1))


