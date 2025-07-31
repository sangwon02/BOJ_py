import sys
input = sys.stdin.readline

n = int(input())

if n%2==0:  # 만약 짝수이면 창영이 승
    print("CY")
else:  # 홀수면 상근이 승
    print("SK")
    
    
n = int(input())

win = [-1]*10001

win[1] = 1 # 상근 승
win[2] = 0 # 창영 승
win[3] = 1 # 상근 승

for i in range(4,n+1):  # DP
    if win[i-1] == 1 or win[i-3] == 1:
        win[i] = 0
    else:
        win[i] = 1

if win[n]==1:
    print('SK')
else:
    print('CY')