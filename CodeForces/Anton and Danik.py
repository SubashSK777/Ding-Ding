n = int(input())
s = input()

anton = 0
danik = 0

for i in s:
    if i == "A":
        anton += 1
    else:
        danik += 1

if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")