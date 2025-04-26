n = int(input())

count = 0

max_count = 0

for i in range(n):
    a, b = map(int, input().split())
    count -= a
    count += b

    max_count = max(count, max_count)

print(max_count)