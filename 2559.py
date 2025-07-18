import sys
input = sys.stdin.readline

n , k = map(int, input().split())
li = list(map(int, input().split()))

sum = [0]  # 누적합 구해서 저장할 리스트
res = -10**10 # 답을 구할 변수

for i in li:
    sum.append(sum[-1] + i)  # 누적합 계산
    
for i in range(n-k+1):
    res = max(res, sum[i+k] - sum[i])  # 구간 합 계산 후 최소값 갱신
print(res)  # 최소값 출력