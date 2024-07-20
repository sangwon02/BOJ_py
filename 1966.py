from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0  # 몇번째로 출력되는지 카운팅 해줄 변수
    
    while queue:
        maxnum = max(queue)  # 큐에 있는 수 중에 가장 큰 값 저장
        num = queue.popleft() # 맨 앞 숫자를 뽑고
        m -= 1  # m의 위치가 땡겨짐

        if num == maxnum:  # 가장 큰 수일 때
            cnt += 1  # cnt에 하나 카운팅 
            if m < 0:  # m이 0보다 작다면
                # 원하는 숫자가 프린팅 되는 경우이니
                print(cnt)  # cnt 출력
                break # while문 종료

        else:  # 가장 큰 수가 아니면
            queue.append(num) # 맨 뒤로 보내고
            if m < 0 :  # 만약 원하는 숫자가 뽑혔다면
                m = len(queue) - 1 # 뒤로 보냄