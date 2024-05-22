import sys
from collections import deque
input = sys.stdin.readline

n = int(input())  # 카드 더미 생성
deq = deque([i for i in range(1,n+1)])

while len(deq) > 1:  # 카드가 하나 남을때 까지 반복
    deq.popleft()  # 가장 위에 있는 카드 제거
    # 가장 위에 있는 카드 맨 밑으로 넣어줌
    card = deq.popleft()
    deq.append(card)
# 답 출력
print(deq[0])