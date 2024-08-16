import sys
import math
import heapq

input = sys.stdin.readline


def dijkstra(graph, n, source, sink):
    dist = [math.inf]*n  # 거리 초기화
    pq = []  # 우선 순위 큐 생성
    dist[source] = 0
    heapq.heappush(pq, (0, source))  # 소스 집어 넣음
    while len(pq) != 0:
        cost, node = heapq.heappop(pq)  # 
        for i in range(1, n):  # 0은 안씀
            nextCost = dist[node] + graph[node][i]  # 현재 거리가
            if nextCost < dist[i]: # 원래 있던 값보다 작다면
                dist[i] = nextCost  # 갱신해줌
                heapq.heappush(pq, (nextCost, i))  # 우선 순위 큐
    return dist[sink]

n, e = map(int, input().split())  # 정점의 개수와 간선의 개수 입력 받고
graph = [[math.inf] * (n+1) for _ in range(n+1)]  # 초기값을 무한대로 저장해 그래프 생성
for _ in range(e):  # a에서 부터 b까지의 거리 c 입력 받아 저장
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    
v1, v2 = map(int, input().split())  # 반드시 거쳐야 하는 번호 입력 받음 



# v1, v2의 순서로 가는 경우와 v2, v1의 순서로 가는 경우를 만들어
num1 = dijkstra(graph, n+1, 1, v1) + dijkstra(graph, n+1, v1, v2) + dijkstra(graph, n+1, v2, n)
num2 = dijkstra(graph, n+1, 1, v2) + dijkstra(graph, n+1, v2, v1) + dijkstra(graph, n+1, v1, n)

result = min(num1, num2)  # 둘 중 최솟값을 저장하고

if result != math.inf:  # 만약 거리가 측정가능하다면
    print(result)  # 출력
else:  # 측정 불가라면
    print(-1)  # -1 출력
