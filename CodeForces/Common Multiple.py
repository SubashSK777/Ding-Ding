n = int(input())

for i in range(n):
    a = int(input())
    arr = list(map(int, input().split()))
    print(len(set(arr)))