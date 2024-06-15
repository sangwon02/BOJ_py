from itertools import combinations  # combinations함수를 불러옴
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numli = []

for i in range(1, n+1):  # 1부터 n까지의 정수가 들어있는 리스트 생성 
    numli.append(i)
    
result = list(combinations(numli, m))  # combinations함수를 이용해 조합을 사용한 경우의 수 저장

for i in result:  # result에 있는 리스트들의 수를 원하는 형식에 맞게 출력
    for j in i:
        print(j, end = " ")
    print("")