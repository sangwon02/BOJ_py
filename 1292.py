n1, n2 = map(int, input().split())
li = [0]

for i in range(50):
    for j in range(i):
        li.append(i)

print(sum(li[n1:n2+1]))