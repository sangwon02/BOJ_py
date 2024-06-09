import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque([])  # deque를 이용해 시간초과 문제 해결

for i in range(n):
    com = input().split()
    
    if com[0] == 'push':  # push일 때
        queue.append(com[1])

    elif com[0] == 'pop':  # pop일 때
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif com[0] == 'size':  # size일 때
        print(len(queue))

    elif com[0] == 'empty':  # empty일 때
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif com[0] == 'front':  # front일 때
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif com[0] == 'back':  # back일 때
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])




