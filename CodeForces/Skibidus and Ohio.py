n = int(input())

for i in range(n):
    s = input()
    f = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            f = 1

    if f == 1:
        print(1)
    else:
        print(len(s))
