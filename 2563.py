arr = [[0] * 101 for _ in range(101)]

n = int(input())

for i in range(n):
    N, M = map(int, input().split())
    for j in range(N , N+10):
        for k in range(M, M+10):
            arr[j][k] = 1

s = 0
for i in arr:
    s += i.count(1)

print(s)