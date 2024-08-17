import heapq
import math
import sys

input = sys.stdin.readline

INF = math.inf 
n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(1, m + 1):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))

start, end = map(int, input().strip().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        curCost, curNode = heapq.heappop(q)
        if distance[curNode] < curCost:
            if curNode == end:
                break
            else:
                continue
        for i in graph[curNode]:
            cost = curCost + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance[end])