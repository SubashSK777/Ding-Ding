s = input()

lst = [i for i in s]

res = []

while lst != []:
    if lst[0] == '.':
        lst.pop(0)
        res.append('0')

    else:
        if lst[0] == '-':
            if lst[1] == '.':
                lst.pop(0)
                lst.pop(0)
                res.append('1')
            
            elif lst[1] == '-':
                lst.pop(0)
                lst.pop(0)
                res.append('2')

print("".join(res))