import sys
from fractions import Fraction  # 기약분수로 나타내는 함수를 가져옴

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))  # 링의 반지름 입력 받음
for i in range(1,n):
    if Fraction(li[0], li[i])%1 == 0:  # 만약 기약분수가 아닌 정수로 나온다면
        print(Fraction(li[0], li[i]),end="")  # 정수 출력 후
        print("/1")  # '/1'를 붙여서 출력
    else:  # 아니면 그냥 출력
        print(Fraction(li[0], li[i]))