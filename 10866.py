import sys
input = sys.stdin.readline

n = int(input())
deque = []  # 리스트로 덱 만듬

for i in range(n):
    command = []
    command = input().split() # 명령어 입력 받음
    
    if command[0] == 'push_front':  # push_front 일 때
        deque.insert(0, int(command[1]))  # 덱의 앞에 정수 저장
        
    elif command[0] == 'push_back':  # push_back 일 때
        deque.append(int(command[1])) # 덱의 뒤에 정수 저장
        
    elif command[0] == 'pop_front':  # pop_front 일 때
        if len(deque) == 0:  # 비어있으면 -1 출력
            print(-1)
        else:
            print(deque[0])  # 맨 앞에 있는 정수 출력 후
            del deque[0]  # 맨 앞에 있는 정수 제거
    
    elif command[0] == 'pop_back':  # pop_back 일 때
        if len(deque) == 0:  # 비어있으면 -1 출력
            print(-1)
        else:
            print(deque[-1])  # 맨 뒤에 있는 정수 출력 후
            del deque[-1]  # 맨 뒤에 있는 정수 제거
            
    elif command[0] == 'front':  # front 일 때
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])  # 맨 앞에 있는 정수 출력
            
    elif command[0] == 'back':  # back 일 때
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])  # 맨 뒤에 있는 정수 출력
        
        
    elif command[0] == 'size':  # size 일 때
        print(len(deque))  # 스택의 크기 출력
        
    elif command[0] == 'empty':  # empty 일 때
        if len(deque) == 0:  # 비어있으면 1 출력
            print(1)
        else:  # 안 비어있으면 0 출력
            print(0)