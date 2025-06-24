import sys
input = sys.stdin.readline

n = int(input())

arr = []  
for i in range(n):  
    x, y = map(int, input().split())  # x, y 죄표 입력 받고
    arr.append([y, x])  # 넣을 때는 반대로 해서(y, x) 넣어줌
    
arr.sort(reverse=False)  # sort를 통해 정렬

for i in arr:  # 죄표 출력
    print(i[1], i[0])  # 출력은 (x, y)