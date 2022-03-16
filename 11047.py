n1, n2 = map(int, input().split())
li = []
cnt = 0


for i in range(n1):
    li.append(int(input()))

sorted(li)

for j in range(n1-1, -1, -1):
    cnt = cnt + n2//li[j]
    n2 = n2%li[j]
        

print(cnt)