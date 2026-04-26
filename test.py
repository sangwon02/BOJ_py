n = int(input())

visited = [-1]*n
cnt = 0

def check(now_row):
    for row in range(now_row):
        if visited[now_row] == visited[row] or 