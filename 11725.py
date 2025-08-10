import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
# 방문 여부 체크와 부모 노드 저장을 한 번에 처리할 리스트
parent = [0] * (N + 1)

# 트리정보 입력
for _ in range(N - 1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
# 루트 노드는 방문했음을 표시
parent[1] = 1

#빌 때까지 탐색
while queue:
    current_node = queue.popleft()
    
    for neighbor in graph[current_node]:
        # 아직 방문하지 않은 노드
        if parent[neighbor] == 0:
            # 부모를 현재 노드로 기록
            parent[neighbor] = current_node
            # 다음에 탐색할 노드로 큐에 추가
            queue.append(neighbor)

# 2번 노드부터 N번 노드까지의 부모를 순서대로 출력
for i in range(2, N + 1):
    print(parent[i])