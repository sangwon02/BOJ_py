import sys
input = sys.stdin.readline  

w, h = map(int, input().split())  # 가로와 세로 크기 입력
n = int(input())  # 추가된 선의 수 입력
width = [0, w]  # 가로 길이 리스트
height = [0, h]  # 세로 길이 리스트

for _ in range(n): #n개의 선을 입력받음
    a, b = map(int, input().split())  # 선의 방향과 위치 입력 받음
    if a == 0: 
        height.append(b)  # 세로 위치 추가
    elif a == 1: 
        width.append(b)  # 가로 위치 추가

#가로와 세로 위치 정렬
width.sort()
height.sort()

res = 0  # 정답을 닮을 변수

#가로와 세로의 각 구간을 계산하여 정답을 찾음
for i in range(len(width)-1):
    for j in range(len(height)-1):
        x = width[i+1] - width[i]  # 가로 간격 계산
        y = height[j+1] - height[j]  # 세로 간격 계산
        res = max(res, x * y)  # 최대 면적 계산

print(res)  #결과 출력
