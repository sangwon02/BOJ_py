import heapq 
import math   
import sys    

input = sys.stdin.readline 

INF = math.inf  # 무한대를 의미하는 상수 정의
n = int(input())  # 노드의 수 입력
m = int(input())  # 엣지의 수 입력

# 그래프 초기화: 인접 리스트로 표현
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)  # 거리 정보를 무한대로 초기화

# 엣지 정보 입력
for i in range(1, m + 1):
    a, b, c = map(int, input().strip().split())  # 엣지의 시작 노드, 끝 노드, 비용 입력
    graph[a].append((b, c))  # 그래프에 엣지 추가

start, end = map(int, input().strip().split())  # 시작 노드와 도착 노드 입력

def dijkstra(start):
    q = []  # 우선순위 큐 초기화
    heapq.heappush(q, (0, start))  # 시작 노드와 비용 0을 큐에 추가
    distance[start] = 0  # 시작 노드의 거리는 0으로 설정

    while q:  # 큐가 빌 때까지 반복
        curCost, curNode = heapq.heappop(q)  # 비용이 가장 적은 노드 꺼내기
        
        if distance[curNode] < curCost:  # 현재 노드까지의 거리보다 더 큰 비용이 들어오면 무시
            continue  # 다음 반복으로 넘어가기

        # 현재 노드와 연결된 노드들 탐색
        for i in graph[curNode]:
            cost = curCost + i[1]  # 현재 비용에 연결된 노드의 비용 추가
            if distance[i[0]] > cost:  # 더 짧은 경로가 발견되면
                distance[i[0]] = cost  # 거리 업데이트
                heapq.heappush(q, (cost, i[0]))  # 큐에 새로운 경로 추가

dijkstra(start)  # 다익스트라 알고리즘 실행
print(distance[end])  # 도착 노드까지의 최단 거리 출력
