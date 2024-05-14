import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))

left, right = 0, 1 
cnt = 0
while right<=n and left<=right:
    sum_nums = A[left:right]  # 인덱스를 슬라이싱해 합 구함
    total = sum(sum_nums)  # 슬라이싱 해준 값들을 더한 것들이

    if total == m:  # m과 같다면
        cnt += 1
        right += 1

    elif total < m:  # m보다 작다면
        right += 1

    else:  # m보다 크다면
        left += 1  # 왼쪽 부분 슬라이싱 해줄 부분 +1

print(cnt)  # 몇개의 경우의 수가 있는지 출력