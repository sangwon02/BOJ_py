import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = sorted(list(map(int,input().split())))

total = []

def dfs(s):
    if len(total) == m:
        print(*total)
        return

    for i in range(s,n):
        total.append(li[i])
        dfs(i+1)
        total.pop()

dfs(0)