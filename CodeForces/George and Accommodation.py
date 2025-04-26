n = int(input())
cnt = 0
for i in range(n):
    
    p, q = map(int, input().split())
    r = q - p
    if r > 1:
        cnt += 1

print(cnt)
