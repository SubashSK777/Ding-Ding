n = int(input())

for i in range(n):

    s = input()
    set_s = list(s)

    if len(set_s) > 10:
        print(f"{set_s[0]}{len(set_s) - 2}{set_s[-1]}")

    else:
        print(s)