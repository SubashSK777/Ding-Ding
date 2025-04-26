n = int(input())

if n % 2 == 0:
    odd = n // 2
    even  = n // 2

else:
    odd = n // 2 + 1
    even = n // 2

odd_sum = odd * odd
even_sum = even * (even + 1)

print(even_sum - odd_sum)