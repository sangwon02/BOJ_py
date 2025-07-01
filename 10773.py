import sys
input = sys.stdin.readline

stack = []  # 리스트를 이용해 스택 생성

k= int(input())  # k입력 받고

for i in range(k):  # k번 정수를 입력 받는다.
    num = int(input())
    
    if num == 0:  # 만약 0이면 가장 최근에 쓴 수를 지우고
        stack.pop()
    else:  # 0이 아니면
        stack.append(num)  # 스택의 규칙을 지키면서 stack에 삽입한다.
        
print(sum(stack))  # 총합 출력