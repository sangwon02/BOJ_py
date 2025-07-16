import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

min_cost = float('inf')  # 최소 비용 저장

def dfs(start, now, count, cost, visited):
    global min_cost
    # 모든 도시를 방문했으면 출발 도시로 복귀
    if count == N:
        if W[now][start] != 0:# 마지막에서 출발점으로 갈 수 있는 경우만
            min_cost = min(min_cost, cost + W[now][start])
        return

    for next in range(N):
        # 아직 방문하지 않았고, now에서 next로 갈 수 있는 경우만
        if not visited[next] and W[now][next] != 0:
            visited[next] = True
            dfs(start, next, count + 1, cost + W[now][next], visited)
            visited[next] = False  # 백트래킹

# 각 도시를 출발점으로 삼아 완전탐색
for i in range(N):
    visited = [False] * N
    visited[i] = True
    dfs(i, i, 1, 0, visited)

print(min_cost)
