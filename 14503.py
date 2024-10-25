import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 현재 x좌표 현재 y좌표 현재 방향
x, y, d = map(int, input().split())

# 방향을 나타내는 배열 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]  # x좌표
dy = [0, 1, 0, -1]  # y좌표


map = [list(map(int, input().split())) for _ in range(n)]

cnt = 0  # 청소한 칸의 수 카운트 하는 변수

while True:
    if map[x][y] == 0:  # 현재 위치가 청소되지 않은 경우
        map[x][y] = 2  # 현재 위치 청소
        cnt += 1  # 청소한 칸 수 증가

    switch = False  # 방향 바꾸기 여부를 체크하는 변수
    for i in range(4):
        # 왼쪽으로 방향 전환
        d = (d + 3) % 4 
        nx, ny = x + dx[d], y + dy[d]  # 새 좌표 계산
        
        # 새 좌표가 맵 안에 있고, 청소되지 않은 경우
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0:
            x, y = nx, ny  # 좌표 업데이트
            switch = True  # 방향을 변경했음을 표시
            break

    # 어디로도 이동할 수 없는 경우
    if not switch:
        nx, ny = x - dx[d], y - dy[d]  # 뒤로 한 칸 이동
        # 뒤로 이동할 수 있다면
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] != 1:
            x, y = nx, ny  # 좌표 업데이트
        else:
            break  # 이동할 수 없으므로 종료


print(cnt)  # 청소한 칸의 수 출력
