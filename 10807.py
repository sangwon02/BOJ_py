x = int(input())

l = list(map(int, input().split()))

x1 = int(input())
sum = 0
for i in l:
    if i == x1:
        sum += 1

print(sum)