n = int(input())

count = 0

for i in range(n):
    a = input()
    if '+' in a:
        count += 1
    else:
        count -= 1


print(count)