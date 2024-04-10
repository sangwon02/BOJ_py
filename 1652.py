import sys
input = sys.stdin.readline

n = int(input())  # n을 입력 받고
li = []
horizontal = 0  # 가로로 잘 수 있는 경우
vertical = 0  # 세로로 잘 수 있는 경우

for i in range(n):  # 방 구조를 리스트에 입력 받는다.
    st = input()
    li.append(st)

for i in range(n):  # 방을 n*n으로 나누어 조사한다.
    cnt1 = 0  # 가로 조사 때 카운트할 변수
    cnt2 = 0  # 세로 조사 때 카운트할 변수
    for j in range(n):
        # 가로로 누울 수 있는 경우 찾음
        if li[i][j] == '.':  # 만약 짐이 없으면
            cnt1 += 1  # cnt1 +1
        else:  # 만약 짐이 있다면 
            cnt1 = 0  # 여기서는 못 누우니 cnt1 = 0
        if cnt1 == 2:  # 만약 연속으로 짐이 없다면
            horizontal += 1  #가로로 누울 수 있는 경우 +1

        # 위와 같은 코드인데 세로로 조사함
        if li[j][i] == '.':
            cnt2 += 1
        else:
            cnt2 = 0
        if cnt2 == 2:
            vertical += 1


print(horizontal, vertical)  # 답 출력

