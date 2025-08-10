import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 

# 깊이 우선 탐색(DFS) 함수
def dfs(t):
    global cnt
    visited[t] = cnt # 현재 정점에 방문 순서 기록
    line[t].sort() # 인접 정점 오름차순 정렬
    
    # 인접 정점 순회
    for i in line[t]:
        if visited[i] == 0: # 미방문 정점이라면
            cnt += 1
            dfs(i) # 재귀적으로 탐색

N, M, R = map(int, input().split())

line = [[] for _ in range(N+1)]
visited = [0]*(N+1) 
cnt = 1  # 방문 순서

# 간선 정보로 그래프 구성
for _ in range(M):
    a, b = map(int, input().split())
    line[a].append(b) 
    line[b].append(a) 
    
# 시작점 R부터 DFS 실행
dfs(R)

# 방문 순서 출력
for i in range(1, N+1):
    print(visited[i])