n = int(input())

count = 0

for i in range(n):
    
    a = list(map(int, input().split()))
    if a.count(1) > 1:
        count += 1

print(count)