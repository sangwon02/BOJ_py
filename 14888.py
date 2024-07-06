import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
symbol = list(map(int, input().split()))

def dfs(depth, total, plus, minus, multi, divide):
    global maxresult, minresult
    if depth == n: # 모든 사칙연산 기호를 사용했다면
        maxresult = max(total, maxresult) # maxresult의 값과 비교해 저장
        minresult = min(total, minresult) # minresult의 값과 비교해 저장
        return
        
    if plus:  # 덧셈 기호가 남아있다면
        dfs(depth + 1, total + num[depth], plus - 1, minus, multi, divide)
        
    if minus:  # 뺄셈 기호가 남아있다면
        dfs(depth + 1, total - num[depth], plus, minus - 1, multi, divide)
        
    if multi:  # 곱셈 기호가 남아있다면
        dfs(depth + 1, total * num[depth], plus, minus, multi - 1, divide)
        
    if divide:  # 나눗셈 기호가 남아있다면
        dfs(depth + 1, int(total / num[depth]), plus, minus, multi, divide-1)

maxresult = -1000000000
minresult = 1000000000

dfs(1, num[0], symbol[0], symbol[1], symbol[2], symbol[3]) # total 초기값은 첫번째 정수
# 정답 출력
print(maxresult)
print(minresult)