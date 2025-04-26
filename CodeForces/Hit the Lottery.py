n = int(input())

count = 0

ops = [100, 20, 10, 5, 1]

i = 0

while n != 0:
    count += n // ops[i]
    n %= ops[i]
    i += 1

print(count)