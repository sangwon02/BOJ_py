# https://cochin-man.tistory.com/26 참고
import sys, heapq, math
input = sys.stdin.readline

n, m = map(int,input().split())
INF = math.inf 
graph = [[] for _ in range(n+1)]  # graph 리스트 선언
distance = [INF]*(n+1)    # 각 지점의 거리를 노드의 갯수만큼 무한대로 생성

# 노드 위치와 비용을 입력 받는다.
for i in range(m): 
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(s):
    q = [] 
    distance[s] = 0 # 자신과의 거리는 0
    heapq.heappush(q,(0,s)) # q에 거리와 위치 입력 받음
    while q: 
        dist, cur = heapq.heappop(q) 
        if distance[cur] < dist: # 현재 있는 최솟값보다 크다면 다음으로 넘어감
            continue 
        for next in graph[cur]:  # 이웃 되어있는 노드를 확인합니다.
            cost = dist + next[1]  # dist 출발 지점에서 현재 노드까지의 거리 + 현재 노드에서 다음 노드까지의 거리
            if cost < distance[next[0]]:  # 더 작으면 갱신
                distance[next[0]] = cost  
                heapq.heappush(q,(cost, next[0]))  

    return distance[n]

print(dijkstra(1))  # 답 출력