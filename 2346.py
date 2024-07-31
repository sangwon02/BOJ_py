import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = deque(list(map(int, input().split())))  # 풍선의 수 입력 받음
numbers = deque([i for i in range(1, n + 1)])  # 풍선의 번호 저장
result = []  # 답을 저장 할 리스트

while d:  # 풍선이 남아있다면 계속
    num = d.popleft()  # 풍선을 터트리고
    result.append(numbers.popleft())  # 터진 풍선의 번호 저장
    # 이때 이미 num이 음수 야수로 구분되어 있기에 풍선이 돌때 구분할 필요 없음
    if num > 0:  # 만약 0보다 크다면
        d.rotate(-(num-1))  # num-1을 오른쪽으로 이동
        numbers.rotate(-(num-1))
    else: # 만약 음수라면
        d.rotate(-num)  # num을 왼쪽으로 이동 
        numbers.rotate(-num)
        
print(*result)  # 답 출력