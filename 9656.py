import sys
input = sys.stdin.readline

n = int(input()) # 돌의 개수를 입력 받고

if n%2 == 0:  # 돌의 개수가 짝수이면
    print("SK")  # 상근이 승리
if n%2 == 1:  # 홀수이면
    print("CY")  # 창영이 승리