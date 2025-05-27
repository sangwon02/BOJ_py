import sys
import heapq

input = sys.stdin.readline

# 지름길의 개수 N과 고속도로의 길이 D를 입력받음
N, D = map(int, input().split())
shortcuts = [tuple(map(int, input().split())) for _ in range(N)]

# 각 위치까지의 최소 거리 초기화
dist = [float('inf')] * (D + 1)  # 초기값은 무한대
dist[0] = 0  # 출발점의 거리 0으로 설정

# 우선순위 큐 초기화 
pq = [(0, 0)]  # 시작점

# 우선순위 큐가 빌 때까지 반복
while pq:
    cur_d, cur = heapq.heappop(pq)  # 현재 거리와 위치를 꺼냄
    if cur_d > dist[cur]:  # 이미 더 짧은 경로가 발견되면 무시
        continue

    # 현재 위치에서 한 칸 이동
    if cur + 1 <= D and cur_d + 1 < dist[cur + 1]:
        dist[cur + 1] = cur_d + 1  # 최소 거리 업데이트
        heapq.heappush(pq, (dist[cur + 1], cur + 1))  # 큐에 추가

    # 지름길 사용 여부 체크
    for start, end, shortcut_len in shortcuts:
        # 현재 위치가 지름길의 시작점이고, 도착 위치가 D 이내일 때
        if cur == start and end <= D:
            # 지름길을 사용할 경우 거리 업데이트
            if cur_d + shortcut_len < dist[end]:
                dist[end] = cur_d + shortcut_len  # 최소 거리 업데이트
                heapq.heappush(pq, (dist[end], end))  # 큐에 추가

# 답 출력력
print(dist[D])
