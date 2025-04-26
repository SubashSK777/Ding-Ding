n = int(input())

arr = list(map(int, input().split()))

res = sum(arr) / n

print("%.12f" %(res))