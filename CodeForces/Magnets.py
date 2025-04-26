n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

c = 0

for i in range(n - 1):
    if arr[i] != arr[i + 1]:
        c += 1

print(c + 1)