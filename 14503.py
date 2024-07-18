import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

map = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

while True:
    if map[x][y] == 0:
        map[x][y] = 2
        cnt += 1

    switch = False
    for i in range(4):
        d = (d + 3) % 4 
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0:
            x, y = nx, ny
            switch = True
            break

    if not switch:
        nx, ny = x - dx[d], y - dy[d]
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] != 1:
            x, y = nx, ny
        else:
            break

print(cnt)
