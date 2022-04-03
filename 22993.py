n = int(input())
li = list(map(int, input().split()))
a = li[0]
li = sorted(li[1:])
cnt = 0

for i in li:
    if a > i:
        a += i
    else:
        cnt = 1
        break

if cnt == 0:
    print("Yes")
else:
    print("No")