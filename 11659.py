import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = list(map(int, input().split()))
sum = [0] # 누적합 구해서 저장할 리스트

# 누적 합 구해두고
num = 0
for i in li:
    num = num + i
    sum.append(num)

# 구간 합 출력
for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])