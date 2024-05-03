import sys
input = sys.stdin.readline

n = int(input()) 
a = set(map(int, input().split()))  # n개의 정수 입력 받음
m = int(input())
num = list(map(int, input().split()))  # m개의 정수 입력 받음

for i in num:  # num에 있는 정수를 하나씩 돌아봄
    if i in a:  # 만약 a안에 있다면
        print(1)  # 1 출력
    else:  # 만약 없다면
        print(0)  # 0 출력