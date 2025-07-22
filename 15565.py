import sys
input = sys.stdin.readline

n, k = map(int, input().split())    
li = list(map(int, input().split()))

res = 10**10 # 가장 작은 연속된 인형 집합 크기
count = 0     # 현재 라이언 인형 수

left = 0
right = 0
if li[right] == 1: count += 1

while right < n:
    # k개의 라이언인 경우 정보 저장
    if count == k:
        res = min(res, right - left + 1)
        if li[left] == 1: count -= 1
        left += 1
    #  k개 이하 라이언 경우 
    else:
        right += 1
        if right < n and li[right] == 1: count += 1

if res == 10**10: # 라이언 인형이 k개 이상 없을 경우
    print(-1)
else:  # 답 출력
    print(res)
