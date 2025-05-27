import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*1001 # n은 1 ≤ n ≤ 1,000
dp[1] = 1  # n이 1인 경우
dp[2] = 2  # n이 2인 경우

for i in range(3,n+1): 
    dp[i] = (dp[i-1] + dp[i-2]) % 10007 # 점화식을 사용해서 n까지의 경우의 수를 구한다.
    
print(dp[n])