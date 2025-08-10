import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map_li = []
for i in range(n):
    map_li.append(list(map(int, input().split())))

dx = [1, 0, 1]
dy = [0, 1, 1]

check = [ [0]*m for _ in range(n) ] #  dp map
check[0][0] = map_li[0][0]

for i in range(n):
    for j in range(m):
        for k in range(3):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < n and 0 <= y < m:
                num = check[i][j] + map_li[x][y]
                if check[x][y] < num:
                    check[x][y] = num

print(check[n-1][m-1])