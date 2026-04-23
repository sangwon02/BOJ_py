import sys
input = sys.stdin.readline

n = int(input())
visited = [-1] * n  # visited[i] = i번째 행의 퀸이 놓인 열 번호
cnt = 0  # 가능한 배치 경우의 수

def check(now_row):
    """now_row에 놓은 퀸이 이전 행들의 퀸과 충돌하는지 확인"""
    for row in range(now_row):
        # 같은 열에 있거나, 대각선에 있으면 충돌!
        if visited[now_row] == visited[row] or now_row - row == abs(visited[now_row] - visited[row]):
            return False
    return True  # 충돌 없음!

def dfs(row):
    """row번째 행에 퀸을 놓는 모든 경우를 탐색 (백트래킹)"""
    global cnt
    if row == n:
        # 모든 행에 퀸을 다 놓았으면 성공!
        cnt += 1
    else:
        for col in range(n):
            visited[row] = col  # row행 col열에 퀸 배치 시도
            if check(row):      # 충돌 없으면
                dfs(row + 1)    # 다음 행으로 진행

dfs(0)
print(cnt)