import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
d = deque()
for i in range(1, n+1): # 1부터 n까지 카드 더미를 덱을 이용해 생성
    d.append(i)
    
result = []  # 답을 출력 할 리스트

for i in range(n-1): # n-1번 반복
    result.append(d.popleft()) # 맨 위에 있는 카드를 result에 넣고 삭제
    d.append(d.popleft())  # 맨 위에 있는 카드를 맨 밑으로 넣음
result.append(d.popleft())  # 마지막 남은 카드를 result에 넣고

for i in result:  # 답 출력
    print(i, end=" ")
print("")