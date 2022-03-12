n1, n2 = map(int, input().split())
n = int(input())
li = []
li1 = []

for i in range(n):
    li.append(int(input()))
    li1.append(abs(n2-li[i]))

main = min(li1)

if abs(n2-n1)>=(main+1):
    print(main+1)
else:
    print(abs(n2-n1))

