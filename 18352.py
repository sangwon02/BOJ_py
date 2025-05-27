import heapq
import math
import sys

input = sys.stdin.readline

INF = math.inf
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):  # 그래프에 도시끼리의 정보를 담는다.
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 소스를 집어 넣음
    distance[start] = 0

    while q:  
        cost, node = heapq.heappop(q)  
        if cost > distance[node]:
            continue
        for i in graph[node]:
            nextcost = cost + 1
            if nextcost < distance[i]:  # 현재 거리가 원래 있던 값보다 작다면
                distance[i] = nextcost  # 갱신
                heapq.heappush(q, (nextcost, i))

dijkstra(x)
flag = 0
for i in range(1, (n+1)):  # 만약 최단거리가 k인 도시가 있다면
    if distance[i] == k: # 출력
        print(i)
        flag = 1

if flag == 0:  # 없다면 -1 출력
    print(-1)