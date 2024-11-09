import sys
input = sys.stdin.readline 

n = int(input())  # 테스트 케이스의 개수 입력

for _ in range(n):
    s = input().strip()  # 문자열 입력
    stack = []  # 스택 초기화
    cnt = True 

    for char in s:
        if char == '(':  # 여는 괄호인 경우
            stack.append(char)  # 스택에 추가
        elif char == ')':  # 닫는 괄호인 경우
            if stack:  # 스택에 여는 괄호가 있는 경우
                stack.pop()  # 스택에서 여는 괄호 제거
            else:  # 비어있는 경우
                cnt = False  
                break  # 반복문 종료

    # 스택이 비어있고, cnt가 True이면 올바른 괄호 조합
    if cnt and not stack:
        print("YES")
    else:
        print("NO")