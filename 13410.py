n1, n2 = map(int, input().split())
li = []

for i in range(n2):
    a = n1*(i+1)
    li.append(int(str(a)[::-1]))

print(max(li))