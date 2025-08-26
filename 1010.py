import sys 
import math 
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    print(math.comb(m, n))  # mCn을 구하는 함수를 사용해 바로 출력
