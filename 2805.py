import sys
input = sys.stdin.readline

n = int(input())
s = 0 # 시작 점
e = n # 끝 점

while s <= e: # s가 e보다 크면 종료
    mid = (s + e) // 2 # s와 e의 중간 지점을 찾고
    if mid ** 2 < n:  # 만약 중간 지점의 제곱한 값이 n보다 작으면
        s = mid + 1  # s를 중간 점+1 로 변경
    else:  # 만약 중간 지점의 제곱한 값이 n보다 크면
        e = mid - 1 # s를 중간 점-1 로 변경

print(s)  # 정답 출력