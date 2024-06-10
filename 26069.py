import sys
input = sys.stdin.readline

n = int(input())
rainbow = {"ChongChong"}  # 무지개 춤을 추는 총총이를 집합에 넣어두고

for i in range(n):
    a, b = input().split()  # 두 사람의 이름을 입력 받아
    if (a in rainbow) or (b in rainbow):  # 만약 둘 중에 한명이 무지개 춤을 춘다면
        rainbow.add(a)  # 집합에 넣어준다.
        rainbow.add(b)
        
print(len(rainbow))  # 집합 안에 원소의 개수 출력
