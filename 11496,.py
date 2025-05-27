import sys
input = sys.stdin.readline

def dijkstra(start, end, graph):
    distances = {i: float('inf') for i in range(1, N + 1)}
    distances[start] = 0
    visited = [False] * (N + 1)

    for _ in range(1, N + 1):
        min_distance = float('inf')
        current_vertex = -1
        
        for vertex in range(1, N + 1):
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current_vertex = vertex

        if current_vertex == -1:  # 더 이상 방문할 노드가 없으면 종료
            break

        visited[current_vertex] = True

        # 연결된 모든 노드 확인
        for neighbor in graph[current_vertex]:
            distance = distances[current_vertex] + 1  # 치환 횟수는 1 증가

            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances[end] if distances[end] != float('inf') else -1

a, b = map(int, input().split())
N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 그래프

result = dijkstra(a, b, graph)

print(result)
