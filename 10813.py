N, M = map(int, input().split())

li = []
n2 = 0

for o in range(N):
    li.append(o+1)

for n1 in range(M):
    i, j = map(int, input().split())
    n2 = li[i-1]
    li[i-1] = li[j-1]
    li[j-1] = n2


for n3 in li:
    print(n3, end=" ")