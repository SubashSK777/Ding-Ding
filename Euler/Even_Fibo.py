arr = [0,1]

while (arr[-1] + arr[-2]) < 4000000:
    arr.append(arr[-1] + arr[-2])

res = 0

for i in arr:
    if i % 2 == 0:
        res += i

print(res)