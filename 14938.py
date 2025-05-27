import heapq
import sys

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, graph, items, m):
    distance = [INF] * (len(graph))
    distance[start] = 0
    max_items = 0
    pq = [(0, start)]  # (현재 거리, 노드)

    while pq:
        cur_cost, node = heapq.heappop(pq)
        
        # 현재 노드까지의 거리보다 더 큰 비용이 들어오면 무시
        if cur_cost > distance[node]:
            continue
        
        # m 이내의 거리에서 아이템 수를 계산
        if cur_cost <= m:
            max_items += items[node - 1]  # 인덱스 조정
        
        for neighbor, weight in graph[node]:
            cost = cur_cost + weight
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(pq, (cost, neighbor))
    
    return max_items

n, m, r = map(int, input().split())  # 도시 수, 최대 거리, 도로 수
items = list(map(int, input().split()))  # 각 도시의 아이템 수
graph = [[] for _ in range(n + 1)]

# 도로 정보 입력
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))  # 양방향 도로

res = 0

# 각 도시를 출발점으로 하여 아이템 수를 최대화
for start in range(1, n + 1):
    collected_items = dijkstra(start, graph, items, m)
    res = max(res, collected_items)

print(res)
