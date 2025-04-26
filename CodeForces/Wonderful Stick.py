t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    res, stack = [], []
    for i in range(n):
        stack.append(i + 1)
        if i == n - 1 or s[i] == '>':
            while stack:
                res.append(stack.pop())
    print(*res)
