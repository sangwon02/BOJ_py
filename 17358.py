import sys
input = sys.stdin.readline

n = int(input()) # 컵의 개수 입력 받음
result = 1  # 결과로 출력할 변수
# 컵의 개수가 n(짝수일때) 답은 (n-1)*(n-3)*(n-5)....3*1이다
# for문과 range함수를 이용해 답 저장하고
for i in range(1, n, 2):  
    result *= i

print(result%(10**9+7))  # 출력