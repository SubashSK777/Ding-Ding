n = int(input())

for i in range(n):
    l = int(input())
    s = input()

    z = s.count('0')
    o = len(s) - z


    if l == 1:
        print(0)

    elif o == l or z == l:
        print(l)
        
    elif o != l or z != l:
        print(l + o)
        