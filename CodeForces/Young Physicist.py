n = int(input())

a_sum = b_sum = c_sum = 0

for i in range(n):
    arr = list(map(int, input().split()))

    a_sum += arr[0]
    b_sum += arr[1]
    c_sum += arr[2]

if a_sum == b_sum == c_sum == 0:
    print("YES")
else:
    print("NO")