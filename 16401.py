import sys
input = sys.stdin.readline

m, n = map(int, input().split())
li = list(map(int, input().split()))

start = 1
end = max(li)
result = 0  # 정답을 담을 변수

while start <= end: # start가 end보다 작으면 계속 실행
    total = 0  # 과자를 조카들에게 나누어 줄 수 있는 숫자를 담을 변수
    mid = (start + end) // 2  # 과자를 나눈 후 과자의 길이
    
    
    for i in li:  # 리스트에 있는 값들을 순서대로 꺼내어서
        total += i // mid  # 줄 수 있는 과자들의 수를 total에 더해줌

    if total >= m:  # 만약 나누어 줄 수 있는 과자의 수가 조카보다 많다면
        start = mid + 1  # 더 긴 과자로 줄 수 있는지 탐색
        result = max(mid, result)  # 정답에 과자의 길이 저장
    elif total < m:  # 안된다면
        end = mid - 1  # 더 짧은 길이의 과자를 주는 경우를 탐색

print(result)  # 정답 출력