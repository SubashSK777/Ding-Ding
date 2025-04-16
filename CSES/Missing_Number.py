n = int(input())
val = list(map(int, input().split()))
ex_res = sum([i for i in range(n + 1)])

print(ex_res - sum(val))
