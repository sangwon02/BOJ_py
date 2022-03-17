cnt = 0
li = []
li1 = []

for i in range(7):
    li.append(int(input()))
    if li[i]%2 == 1:
        cnt += li[i]
        li1.append(li[i])
if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(min(li1))
