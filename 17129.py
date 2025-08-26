import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n, m = map(int, input().split()) 

# 맵 정보 입력 (문자열을 한 글자씩 숫자로 바꿔 2차원 리스트로 저장)
island = [list(map(int, list(str(input().rstrip())))) for _ in range(n)]
# 방문 여부 및 거리 저장을 위한 리스트 (0은 미방문 상태)
visited = [[0 for _ in range(m)] for _ in range(n)]

# 상, 하, 좌, 우 4방향 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    flag = False # 음식을 찾았는지 확인하는 신호
    q.append([x, y]) # 시작 위치를 큐에 추가
    visited[x][y] = 1 # 시작 위치 방문 처리 (거리를 1부터 계산)

    while q:
        # 바로 전 탐색에서 음식을 찾았다면 루프 종료
        if flag:
            break
        x, y = q.popleft() # 큐에서 현재 위치를 꺼냄

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위 안이고, 아직 방문 안 했고, 장애물이 아니라면
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and island[nx][ny] != 1:
                # 이전 위치까지의 거리에 1을 더해 현재 위치의 거리 기록
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny]) # 다음 탐색을 위해 큐에 추가
                
                # 만약 음식을 찾았다면
                if island[nx][ny] == 3 or island[nx][ny] == 4 or island[nx][ny] == 5:
                    flag = True # 찾았다는 신호를 True로 변경
                    count_result = visited[nx][ny] - 1 # 최종 걸린 시간 계산
                    break # 현재 위치의 나머지 방향 탐색은 불필요하므로 중단

    if flag:
        print("TAK") # 예
        print(count_result)
    else:
        print("NIE") # 아니오

for i in range(n):
    for j in range(m):
        if island[i][j] == 2:
            bfs(i, j)