import sys
input = sys.stdin.readline

a, b = map(int, input().split())

setA = set(map(int, input().split()))  # 집합의 원소들 입력 받고
setB = set(map(int, input().split()))
ab = setA-setB  # 각 차집합을 만들어준 후
ba = setB-setA

print(len(ab)+len(ba))  # 대칭 차집합의 개수를 출력한다.