num = []

for i in range(9):
    a = int(input())
    num.append(a)
a = num[0]
for n in num:
    if n >= a:
        a = n
b = int(num.index(a))
print(a, b+1)