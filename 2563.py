import sys
input = sys.stdin.readline

arr = [[0] * 101 for _ in range(101)] 
# 일단 문제 조건에 맞게 0으로 가득 찬 2차원 배열(리스트 안에 리스트) 생성

n = int(input())  

for _ in range(n):  # n만큼 좌표 입력 받음
    n1, n2 = map(int, input().split())  # 좌표 받고
    for i in range(n1, n1+10):  
        for j in range(n2, n2+10):
            arr[i][j] = 1 # 좌표에 맞게 색종이의 영역을 1로 바꿔준다.

res = 0  # 정답을 담을 변수
for i in arr:  # 리스트 안에 리스트를 꺼내서
    res += i.count(1)  # 1의 개수를 더해준다.
print(res)  # 정답 출력