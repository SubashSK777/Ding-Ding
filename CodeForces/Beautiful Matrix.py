n = 5

m = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in  range(n):
        if m[i][j] == 1:
            res = abs(i - 2) + abs(j - 2)

print(res)


