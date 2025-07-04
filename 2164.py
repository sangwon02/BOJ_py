from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
d = deque()  # 덱을 생성

for i in range(1,n+1):
    d.append(i)  # 카드 순서대로 만들고

while len(d) != 1:  # d의 크기가 1이면 종료
    d.popleft()  # 왼쪽에 있는 값 제거하고
    d.append(d.popleft())  # 왼쪽에 있는 값 오른쪽에 삽입
    # 반복
    
print(d[0])  # 마지막으로 남은 값 출력