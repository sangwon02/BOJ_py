# 나중에 직접 다시 풀기
import sys
import heapq
input = sys.stdin.readline
MAX = sys.maxsize

N, M = int(input()), int(input())
arr = [[]for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    arr[start].append((cost, end))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    result[start] = 0
    while q:
        cost, city = heapq.heappop(q)
        if result[city] < cost:
            continue
        for ncost, ncity in arr[city]:
            if result[ncity] > cost + ncost:
                result[ncity] = cost + ncost
                heapq.heappush(q, (result[ncity], ncity))
                parent[ncity] = city


start, end = map(int, input().split())
result = [MAX] * (N+1)
parent = [i for i in range(N+1)]

dijkstra(start)
print(result[end])

path = []
temp = end
while True:
    path.append(temp)
    if temp == parent[temp]:
        break
    temp = parent[temp]
print(len(path))
path.reverse()
print(*path)