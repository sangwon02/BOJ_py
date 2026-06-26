import math

N = int(input()) # 토핑의 종류
A,B = map(int, input().split()) # 도우의 가격, 토핑의 가격
dou_cal = int(input()) # 도우의 칼로리
dou_N_cal = dou_cal/A # 1달러당 도우의 칼로리
to_cals = [] # 토핑들의 칼로리
for _ in range(N):
    n = int(input())
    to_cals.append(n)
    
to_cals.sort(reverse=True) # 토핑들의 칼로리 내림차순 정렬

total_cal = dou_cal
cnt = A
for to_cal in to_cals:
    if total_cal/cnt < to_cal/B: # 만약 현재 평균 칼로리보다 더 높은 1달러당 칼로리면
        total_cal += to_cal # 더해줌
        cnt += B
    else:
        break
print(total_cal//cnt) # 1달러당 칼로리출력