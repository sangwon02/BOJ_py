import sys
input = sys.stdin.readline

# n 입력
n = int(input())

# 10001 크기의 리스트 생성
count = [0] * 10001

# n개의 정수를 리스트의 인덱스로 접근하여 개수 세기
for _ in range(n):
    num = int(input())
    count[num] += 1

# n 리스트에 접근해 그 개수만큼 인덱스 출력
for i in range(10001):
    # count[i]이 1 이상이면
    if count[i] != 0:
        # 그 값만큼 출력
        for j in range(count[i]):
            print(i)