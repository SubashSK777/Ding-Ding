n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.pop(0)
y.pop(0)

z = x + y

# f = 0

# for i in range(1, n + 1):
#     if i not in z:
#         f = 1



if (n * (n + 1) // 2) == sum(set(z)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")


