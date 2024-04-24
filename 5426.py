import sys
input = sys.stdin.readline

n = int(input())  # 원하는 실행 횟수 입력 받음

for i in range(n):
    s = input().lstrip()  # 해석해야하는 문자열 입력 받음
    sqrt = int(len(s) ** (1/2))  # 몇*몇 케이스인지 찾기
    # 원하는 해석값 출력
    for j in range(1, sqrt + 1):  
        for t in range(1, sqrt + 1):
            print(s[sqrt*t-j], end="")
    # 마지막 부분 엔터
    print(" ")