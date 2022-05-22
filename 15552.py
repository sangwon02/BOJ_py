import sys #sys를 불러옴

x = int(input()) #정수를 입력 받음

for _ in range(x): #x만큼 반복
    y, z = map(int, sys.stdin.readline().split()) #공백을 구분하여 정수 두개를 받음
    print(y+z) # y+z 출력