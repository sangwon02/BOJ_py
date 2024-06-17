from itertools import product  # product함수를 불러옴
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numli = []

for i in range(1, n+1):  # 1부터 n까지의 정수가 들어있는 리스트 생성 
    numli.append(i)
    
for i in product(numli, repeat=m):  # numli에서 조건에 맞는 수열을 만들어 출력
    for j in i:
        print(j, end = " ")
    print("")