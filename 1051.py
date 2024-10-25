import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n과 m 입력 받고

li = [] # 직사각형의 숫자를 담는 리스트
 
for i in range(n):  # n개의 줄을을 입력 받아 리스트에 저장
    li.append(list(input()))

check = min(n, m)  # n과 m중에 작은 값을 저장(주어진 직사각형 안에서 만들 수 있는 정사각형의 길이는 check 이하)
answer = 0

for i in range(n):  # 직사각형을 탐색 
    for j in range(m):
        for k in range(check):
            # 만약 꼭짓점에 쓰여 있는 수가 모두 같은 정사각형을 찾았다면 넓이를 구한 후 전에 있던 answer값과 비교 후 갱신
            if ((i + k) < n) and ((j + k) < m) and (li[i][j] == li[i][j + k] == li[i + k][j] == li[i + k][j + k]):
                answer = max(answer, (k + 1)**2)
                
print(answer) # 답 출력