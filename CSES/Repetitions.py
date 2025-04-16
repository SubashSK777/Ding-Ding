s = input()

if len(s) == 1:
    print(1)

else:
    l = 0


    res = 0
    max_res = 0

    for i in range(len(s)):
        if s[l] == s[i]:
            res += 1

        else:
            max_res = max(max_res, res)
            res = 1
            l = i

    max_res = max(max_res, res)
    print(max_res)
