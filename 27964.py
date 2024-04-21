import sys
input = sys.stdin.readline

n = int(input())  # 토핑의 개수를 입력 받음

li = list(input().split())  # 피자에 넣을 토핑들을 입력 받음
cheese = []
for i in range(n):
    tooping = li[i]  # 토핑을 하나씩 꺼내서 비교함
    # 만약 뒷부분이 Cheese로 되어 있고 이미 넣은 토핑이 아니면
    if tooping[-6::] == "Cheese" and ((tooping in cheese) == False):
        cheese.append(tooping)  # 치즈 토핑에 추가
if len(cheese) >= 4:  # 만약 치즈 토핑이 4개 이상이면
    print("yummy")  # 야미 출력
else:  # 못 넘으면
    print("sad")  # sad 출력