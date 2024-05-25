import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

li = list(map(int, input().split()))
li.sort()  # 리스트를 오름차순으로 정렬 후
left, right = 0, len(li) - 1  # 양 끝에서 부터 탐색할 변수
cnt = 0
while left < right:  # 리스트의 모든 값을 돌면 종료
    sum = li[left] + li[right]
    if sum < m:  # 만약 두 값의 합이 m보다 작다면
        left += 1  # 왼쪽 인덱스를 오른쪽으로 옮겨서 탐색
    elif sum > m:  # 만약 두 값의 합이 m보다 크다면
        right -= 1  # 오른쪽 인덱스를 왼쪽으로 옮겨서 탐색
    else:  # 만약 두 값의 합이 m이라면
        cnt += 1  # 카운트 +1
        left += 1  # 다음 값을 찾음
        right -= 1
        
print(cnt)
