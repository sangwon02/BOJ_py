import sys
input = sys.stdin.readline

n = int(input())
que = []  # 리스트로 큐 만듬

for i in range(n):
    command = []
    command = input().split() # 명령어 입력 받음
    
    if command[0] == 'push':  # push 일 때
        que.append(int(command[1]))  # 뒤에 큐의 뒷자리에 정수 저장
        
    elif command[0] == 'pop':  # pop 일 때
        if len(que) == 0:  # 비어있으면 -1 출력
            print(-1)
        else:
            print(que[0])  # 맨 앞에 있는 정수 출력 후
            del que[0]  # 맨 앞에 있는 정수 제거
            
    elif command[0] == 'front':  # front 일 때
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])  # 맨 앞에 있는 정수 출력
            
    elif command[0] == 'back':  # back 일 때
        if len(que) == 0:  
            print(-1)
        else:
            print(que[-1])  # 맨 뒤에 있는 정수 출력
        
    elif command[0] == 'size':  # size 일 때
        print(len(que))  # 큐의 크기 출력
        
    elif command[0] == 'empty':  # empty 일 때
        if len(que) == 0:  # 비어있으면 1 출력
            print(1)
        else:  # 안 비어있으면 0 출력
            print(0)
