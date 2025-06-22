import sys
input = sys.stdin.readline

n = int(input())

arr = []  
for i in range(n):  
    x, y = map(int, input().split())  # x, y 죄표 입력 받고
    arr.append([x, y])
    
arr.sort(reverse=False)  # sort를 통해 정렬

for i in arr:  # 죄표 출력
    print(*i)