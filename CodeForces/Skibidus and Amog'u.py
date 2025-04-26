n = int(input())

for i in range(n):
    s = input()
    for i in range(len(s) - 2):
        print(s[i], end="")
    print("i")