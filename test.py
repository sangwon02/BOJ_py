import sys
import heapq
input = sys.stdin.readline


N, D = map(int, input().split())
shortcuts = [tuple(map(int, input().split())) for _ in range(N)]

dist = [float('inf')] * (D + 1)
dist[0] = 0

pq = [(0, 0)]  # (거리, 위치)
while pq:
    cur_d, cur = heapq.heappop(pq)
    if cur_d > dist[cur]:
        continue

    if cur + 1 <= D and cur_d + 1 < dist[cur + 1]:
        dist[cur + 1] = cur_d + 1
        heapq.heappush(pq, (dist[cur + 1], cur + 1))

    for start, end, shortcut_len in shortcuts:
        if cur == start and end <= D:
            if cur_d + shortcut_len < dist[end]:
                dist[end] = cur_d + shortcut_len
                heapq.heappush(pq, (dist[end], end))

print(dist[D])
