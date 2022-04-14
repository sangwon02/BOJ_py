n1, n2 = map(int, input().split())

n2 = str(n2)

n3 = 0
n4 = 0

while n1 != n3:
    n4 += 1
    if n2 in str(n4):
        continue
    n3 += 1

print(n4)