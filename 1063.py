# 체스판의 열을 정의
region = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 왕과 돌의 이동 방향을 정의 (상, 우상, 우, 우하, 하, 좌하, 좌, 좌상)
dxs = [0, 1, 1, 1, 0, -1, -1, -1]
dys = [1, 1, 0, -1, -1, -1, 0, 1]

# 입력으로부터 왕, 돌, 이동 횟수를 받음
king, stone, n = tuple(input().split())
n = int(n)

# 왕과 돌의 초기 위치를 설정 (인덱스는 0부터 시작하므로 1을 더함)
king_x = region.index(king[0]) + 1
king_y = int(king[1])

stone_x = region.index(stone[0]) + 1
stone_y = int(stone[1])

# 방향을 숫자로 매핑
mapper = {
    'T' : 0,   # 상
    'RT' : 1,  # 우상
    'R' : 2,   # 우
    'RB' : 3,  # 우하
    'B' : 4,   # 하
    'LB' : 5,  # 좌하
    'L' : 6,   # 좌
    'LT' : 7   # 좌상
}

# 주어진 위치가 체스판 범위 안에 있는지 확인하는 함수
def in_range(x, y):
    return x >= 1 and x <= 8 and y >= 1 and y <= 8

# 왕과 돌을 이동시키는 함수
def move(dir_num):
    global king_x, king_y, stone_x, stone_y

    # 왕의 새로운 위치 계산
    king_nx = king_x + dxs[dir_num]
    king_ny = king_y + dys[dir_num]

    # 왕이 범위 내에 있는지 확인
    if in_range(king_nx, king_ny):
        king_x = king_nx
        king_y = king_ny
    else:
        return

    # 왕과 돌이 같은 위치에 있을 경우 돌 이동 처리
    if king_x == stone_x and king_y == stone_y:
        stone_nx = stone_x + dxs[dir_num]
        stone_ny = stone_y + dys[dir_num]

        # 돌이 범위 내에 있는지 확인
        if not in_range(stone_nx, stone_ny):
            # 돌이 범위를 벗어나면 왕의 위치를 원래대로 되돌림
            king_x = king_x - dxs[dir_num]
            king_y = king_y - dys[dir_num]
        else:
            # 돌의 위치 업데이트
            stone_x = stone_nx
            stone_y = stone_ny

# 주어진 이동 횟수만큼 반복
for _ in range(n):
    direction = input()  # 이동 방향 입력
    dir_num = mapper[direction]  # 방향 숫자로 변환
    move(dir_num)  # 왕과 돌 이동

# 최종 위치 출력
king_x = region[king_x - 1]  # 왕의 열 정보를 문자열로 변환
print(king_x + str(king_y))  # 왕의 위치 출력

stone_x = region[stone_x - 1]  # 돌의 열 정보를 문자열로 변환
print(stone_x + str(stone_y))  # 돌의 위치 출력
