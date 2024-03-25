N, M = map(int, input().split())

li = []
n2 = 0

for o in range(N):
    li.append(o+1)

for n1 in range(M):
    i, j = map(int, input().split())
    temp = li[i-1:j]
    temp.reverse()
    li[i-1:j] = temp

for n3 in li:
    print(n3, end=" ")