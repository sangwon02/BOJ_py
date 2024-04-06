import sys  

t = int(input())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    result = m
    for j in range(n-1):
        m -= 1
        result = result * m
    for j in range(n):
        result = result / n
        n -= 1
    print(int(result))

import math  # math함수들 불러옴
import sys  

t = int(input())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(math.comb(m, n))  # mCn을 구하는 함수를 사용해 바로 출력
