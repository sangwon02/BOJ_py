import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n과 m 저장
li = [list(map(int, input().split())) for _ in range(n)]  # 2차원 배열 입력 받음
dp = [[0]*(m+1) for _ in range(n+1)]  # dp 배열 생성

for i in range(1, n+1):  # dp에 요구하는 답 저장
    for j in range(1, m+1):
        dp[i][j] = li[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

k = int(input())  # k에 정수를 저장 해둔 후
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]) # 답