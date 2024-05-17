import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    note1 = set  # 수첩1은 순서가 필요없으니 집합으로 생성
    note2 = []  # 수첩2은 순서가 필요하니 리스트로 생성
    n = int(input())
    note1 = set(map(int, input().split()))  # 수첩1 입력 받음
    m = int(input())
    note2 = li = list(map(int, input().split()))  # 수첩2 입력 받음
    
    for j in note2:  # 수첩2에 있는 정수가
        if j in note1:  # 수첩1에 있다면
            print(1)
        else:  # 수첩1에 없다면
            print(0)