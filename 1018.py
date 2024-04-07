import sys
input = sys.stdin.readline

n, m = map(int, input().split())
original = []
cnt = []  # 얼마나 바꿔야 하는지 모든 경우의 수를 넣는 리스트

for _ in range(n):
    original.append(input())

for a in range(n-7): # 8*8로 짜르기 위해 -7를 함
    for b in range(m-7):
        Wcoloring = 0
        Bcoloring = 0
        for i in range(a, a+8):  
            for j in range(b, b+8):
                # i+j가 홀수인지 짝수인지 구분해야함
                # 홀수, 짝수끼리 색이 같아야하기 때문에
                if (i+j)%2 == 0:  # 짝수일 때
                    if original[i][j] == "B": # 만약 검은색이라면
                        Wcoloring += 1  # 흰색으로 칠하는 갯수
                    else:  # 만약 흰색이라면
                        Bcoloring += 1  # 검은색으로 칠하는 갯수 +1
                else:  # 홀수일 때
                    if original[i][j] == "W": # 만약 흰색이라면
                        Wcoloring += 1  # 흰색으로 칠하는 갯수
                    else:  # 만약 검은색이라면
                        Bcoloring += 1  # 검은색으로 칠하는 갯수 +1
        cnt.append(Wcoloring)  # 경우의 수를 cnt에 넣고
        cnt.append(Bcoloring)

print(min(cnt))  #가장 적게 바꿔도 되는 수 출력
