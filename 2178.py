from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))
    
# 이동하는 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque() # 큐 사용
    queue.append((0, 0)) # 0, 0 부터 시작
    
    while queue: # 큐에 남은게 없을 때 까지 실행
        x, y = queue.popleft()
        # 현재 위치에서 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 벗어나면 예외 처리
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우(0인 경우)도 예외 처리
            if graph[nx][ny] == 0:
                continue
            # 처음 방문하는 경우 최단 거리 기록해줌
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 출구의 거리 반환
    return graph[n-1][m-1]

# BFS 실행
print(bfs())