import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())

li = [0]*n  # 신호등 생성

for i in range(b): # 고장난 신호등 입력 받음
    broken = int(input())
    li[broken-1] = 1  # 고장난 신호등은 1로 표시

broken_cnt = 0
for i in range(k):  # 1번부터 k번까지 합을 저장하고
    broken_cnt += li[i]
result = broken_cnt  # 일단 최종 값에 저장

# 전에 탐색한 값에 맨 앞 값을 빼주고 다음 값을 더해주어 다음 k개의 신호등을 탐색
for i in range(1, n - k + 1):
    broken_cnt = broken_cnt - li[i-1] + li[i+k-1]
    if broken_cnt < result:  # 만약 result값보다 작다면
        result = broken_cnt  # result값에 저장

print(result)  # 정답 출력