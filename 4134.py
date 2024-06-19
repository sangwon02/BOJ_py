import sys
import math
input = sys.stdin.readline

def prime_num(n):  # 소수인지 판별하는 함수
    # n까지가 아닌 가운데 약수(제곱근)까지만 비교한다.
    for i in range(2, int(math.sqrt(n))+1):  
        if n % i == 0:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    if n == 0 or n == 1:  # 만약 0, 1일 때는 2 출력
        print(2)
        continue
    # 만약 n이 소수가 아니라면 다음 수가 소수인지 아닌지 무한 반복
    while prime_num(n + cnt) == False:  
        cnt += 1
    print(cnt+n)  # n보다 크거나 같은 소수 중에 가장 작은 수 출력 