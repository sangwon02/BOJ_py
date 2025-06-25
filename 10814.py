import sys
input = sys.stdin.readline

n = int(input())

li = [] # 나이, 이름 담을 리스트


for i in range(n):
    age, name = map(str, input().split())  # 나이와 이름 입력 받고
    li.append([int(age), name])  # 리스트에 넣어줌 (나이는 정수형으로)

li.sort(key=lambda x:x[0]) # 2차원 리스트의 첫번째 값을 기준으로 정렬

for i in li:  # 답 출력
    print(*i)