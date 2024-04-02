import sys
n = int(sys.stdin.readline())
li = []

for i in range(n):  # 좌표값 입력 받고
    x, y = map(int, sys.stdin.readline().split())
    li.append([y, x])  # 리스트에 넣을때는 반대로
    
li = sorted(li)  # 좌표 정렬

for y, x in li:  # 좌표 출력
    print(x, y)