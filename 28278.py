import sys
input = sys.stdin.readline 

stack = []  # 스택 생성

n = int(input()) 

for _ in range(n):
    command = list(map(int, input().split()))  # 명령어 입력 받음
    if command[0] == 1:  # 1 x 시
        stack.append(command[1])  # x를 스택에 추가
        
    elif command[0] == 2:  # 2 시
        if stack:  # 스택에 원소가 있으면
            print(stack.pop())  # 가장 위의 요소를 출력후 제거
        else:
            print(-1)  #-1 출력
            
    elif command[0] == 3:  # 3일 시comm
        print(len(stack))  # 스택의 크기 출력
        
    elif command[0] == 4:  # 4시
        if not stack:  # 스택이 비어있으면
            print(1)  # 1 출력
        else:
            print(0)  # 0 출력
        
    elif command[0] == 5:  # 5 일 시
        if stack:  # 스택이 원소가 들어있으면 
            print(stack[-1])  # 가장 위의 요소를 출력
        else:
            print(-1)  # 스택이 비어있으면 -1 출력
