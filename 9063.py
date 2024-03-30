n = int(input())  # 입력 받을 횟수
x = []
y = []

for i in range(n):
    n1, n2 = map(int, input().split())  # 좌표를 받고
    x.append(n1)  # x의 값을 x리스트에 넣고
    y.append(n2)  # y의 값을 y리스트에 넣는다.

xlen = max(x) - min(x)  # 사각형의 가로 길이를 구하고
ylen = max(y) - min(y)  # 사각형의 세로 길이를 구한다.

print(xlen*ylen)  # 사각형의 넓이를 출력한다.