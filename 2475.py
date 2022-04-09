li = list(map(int, input().split()))
li2 = []

for i in li:
    li2.append(i*i)

a = sum(li2)
print(a%10)