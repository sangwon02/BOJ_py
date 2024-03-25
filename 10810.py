N, M = map(int, input().split())

li = []

for o in range(N):
    li.append(int(0))


for n1 in range(M):
    i, j, k = map(int, input().split())
    for n2 in range(i-1, j):
        li[n2] = k

for n3 in li:
    print(n3, end=" ")