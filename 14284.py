import heapq as hq
import sys
input = sys.stdin.readline

def dijkstra(s, t):
    # 거리 배열 초기화: 모든 노드까지의 거리를 무한대로 설정
    distance = [float('inf') for _ in range(n + 1)]
    distance[s] = 0  # 출발 노드까지의 거리는 0
    heap = [(0, s)]  #힙 초기화

    while heap:
        curr_cost, curr_node = hq.heappop(heap)  # 비용이 가장 적은 노드 선택
        if distance[curr_node] < curr_cost:  # 이미 처리된 노드라면 무시
            continue
        
        # 현재 노드와 연결된 모든 노드 확인
        for next_node, next_cost in graph[curr_node]:
            total_cost = next_cost + curr_cost  # 새로운 경로의 총 비용 계산
            if total_cost < distance[next_node]:  # 더 짧은 경로가 발견된 경우
                distance[next_node] = total_cost  # 거리 업데이트
                hq.heappush(heap, (total_cost, next_node))  # 힙에 추가

    return distance[t]  # 목표 노드까지의 최단 거리 반환

# 노드 수와 간선 수 입력
n, m = map(int, input().split())
# 그래프 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())  # 간선 정보 입력
    graph[a].append([b, c])  # 방향 그래프 구성
    graph[b].append([a, c])  # 방향 그래프 구성 (양방향)

s, t = map(int, input().split())
print(dijkstra(s, t))