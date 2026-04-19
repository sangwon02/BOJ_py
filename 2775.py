import sys
input = sys.stdin.readline

# 아파트 문제 (백준 2775)
# k층 n호에 사는 사람 수 구하기
# 규칙: k층 n호 = (k-1)층 1호 ~ n호까지의 합

t = int(input())

for _ in range(t):
    k = int(input())   # 층
    n = int(input())   # 호

    # dp[층][호] = 그 방에 사는 사람 수
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # 0층 초기화: 1호=1명, 2호=2명, 3호=3명 ...
    for j in range(1, n + 1):
        dp[0][j] = j

    # 1층부터 k층까지 채우기
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            # i층 j호 = i층 (j-1)호 + (i-1)층 j호
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    print(dp[k][n])