import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]

# 시작 좌표
x, y = n//2, n//2

# 토네이도가 이동하는 거리
length = [i//2+1 for i in range(n*2-1)]
# 서 남 동 북
dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# 토네이도가 이동 할 때 흩어지는 먼지들
flutter = [[(-1, 1, 0.01), (1, 1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05), (0, -1, 0.55)],
                [(-1, -1, 0.01), (-1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (1, -1, 0.1), (1, 1, 0.1), (2, 0, 0.05), (1, 0, 0.55)],
                [(-1, -1, 0.01), (1, -1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (-1, 1, 0.1), (1, 1, 0.1), (0, 2, 0.05), (0, 1, 0.55)],
                [(1, -1, 0.01), (1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (-1, -1, 0.1), (-1, 1, 0.1), (-2, 0, 0.05), (-1, 0, 0.55)]]

rotation, move, direction = 0, 0, 0  
result = 0
while (x, y) != (0, 0):

    if move == length[rotation]:
        move = 0
        direction += 1
        direction %= 4
        rotation += 1
    
    nx = x + dxy[direction][0]
    ny = y + dxy[direction][1]
    
    #  이동할 모래
    sand = map[nx][ny]
    
    total_move_sand = 0
    # 토네이도가 지나가며 모래가 흩날림
    for dx, dy, percentage in flutter[direction]:
        # α인 경우
        if percentage == 0.55:
            move_sand = sand-total_move_sand
        else:
            move_sand = int(sand*percentage)

        move_sand_x, move_sand_y = nx + dx, ny + dy
        total_move_sand += move_sand
        

        if 0<=move_sand_x<n and 0<=move_sand_y<n:
            map[move_sand_x][move_sand_y] += move_sand
        else:
            result += move_sand
            
    x, y = nx, ny
    move += 1

print(result)
