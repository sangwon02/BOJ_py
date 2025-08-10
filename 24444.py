import sys
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# 오름차순 방문을 위해 미리 정렬
for i in range(1, N + 1):
    graph[i].sort()

def bfs(start_node):
    global count
    queue = [start_node]
    visited[start_node] = count
    
    while queue:
        current_v = queue.pop(0)
        
        for next_v in graph[current_v]:
            if visited[next_v] == 0:
                count += 1
                visited[next_v] = count
                queue.append(next_v)

bfs(R)

for i in range(1, N + 1):
    print(visited[i])