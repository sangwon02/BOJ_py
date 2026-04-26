import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000000000)

M, N = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

arr = []

for _ in range(M):
    row = [int(num) for num in input().strip()]
    arr.append(row)
    
check = [[0]*N for _ in range(M)]

def dfs(y, x):
    check[y][x] = 1
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if ny < 0 or ny >= M or nx < 0 or nx >= N:
            continue
        if arr[ny][nx] == 1:
            continue
        if check[ny][nx] == 1:
            continue
        
        dfs(ny, nx)
        
for i in range(N):
    if arr[0][i] == 0 and check[0][i] == 0:
        dfs(0, i)
for i in range(N):
    if check[-1][i] == 1:
        print("YES")
        exit()
        
print("NO")
    