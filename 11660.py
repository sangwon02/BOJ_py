import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nummap = [[0]*(n + 1)]

for _ in range(n):
    nums = [0] + [int(x) for x in input().split()]
    nummap.append(nums)

for i in range(1, n + 1):
    for j in range(1, n):
        nummap[i][j + 1] += nummap[i][j]


for j in range(1, n + 1):
    for i in range(1, n):
        nummap[i + 1][j] += nummap[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(nummap[x2][y2] - nummap[x1 - 1][y2] - nummap[x2][y1 - 1] + nummap[x1 - 1][y1 - 1])