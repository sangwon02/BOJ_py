import sys
input = sys.stdin.readline


while True:
    stack = []  # 스택 생성
    str = input().rstrip()  # 문자열 입력 받음
    
    if str == ".":  # "."만 입력 받으면
        exit()  # 프로그램 종료
    
    for i in str:  # 문자열의 문자를 하나씩 돌면서
        if i == "(":   # "(" 이면 스택 방식으로 삽입
            stack.append("(")
            
        elif i == "[":  # "[" 이면 스택 방식으로 삽입
            stack.append("[")
            
        elif i == ")":  # 닫는 ")" 이면
            if stack and stack[-1] == "(": # 만약 여는 괄호 "(" 가 있다면 계속 진행
                stack.pop()
            else:  # 없다면
                print("no") # no 출력 후 종료
                break
            
        elif i == "]":  # 닫는 "]" 이면
            if stack and stack[-1] == "[": # 만약 여는 괄호 "[" 가 있다면 계속 진행
                stack.pop()
            else:  # 없다면
                print("no") # no 출력 후 종료
                break
            
        elif i == ".": # "."이 나오면 문자열이 끝난 것이니 
            if stack:  # 만약 아직 닫히지 않은 괄호가 있다면
                print("no") # no 출력
            else:
                print("yes")  # yes 출력
