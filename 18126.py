import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
# 그래프는 (연결된 노드, 거리) 쌍을 저장
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 1번 방에서부터 각 방까지의 거리를 저장할 리스트
distance = [-1] * (N + 1)

def bfs(start_node):
    queue = deque([start_node])
    distance[start_node] = 0 # 시작점의 거리는 0
    
    while queue:
        current_node = queue.popleft()
        
        # 현재 노드와 연결된 다른 노드들을 확인
        for neighbor, weight in graph[current_node]:
            # 아직 방문하지 않은 노드라면
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current_node] + weight
                queue.append(neighbor)

# 1번 방에서 BFS 시작
bfs(1)

print(max(distance))