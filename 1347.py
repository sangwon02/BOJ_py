import sys
input = sys.stdin.readline

n = int(input())
moves = input()

# 큰 미로판을 가정하고 중앙에서 시작
# (50, 50)을 시작점으로 사용
grid = [['#'] * 101 for _ in range(101)]
x, y = 50, 50

# 0(북), 1(동), 2(남), 3(서)
# 남쪽을 보고 시작하므로 direction = 2
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
direction = 2

# 시작 위치 표시
grid[y][x] = '.'

# 이동 시뮬레이션
for move in moves:
    if move == 'R':
        direction = (direction + 1) % 4
    elif move == 'L':
        direction = (direction - 1 + 4) % 4
    elif move == 'F':
        x += dx[direction]
        y += dy[direction]
        grid[y][x] = '.'

# '.'이 찍힌 최소, 최대 좌표 찾기
min_r, max_r = 101, -1
min_c, max_c = 101, -1
for r in range(101):
    for c in range(101):
        if grid[r][c] == '.':
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)

# 결과 출력
for r in range(min_r, max_r + 1):
    print("".join(grid[r][min_c:max_c + 1]))