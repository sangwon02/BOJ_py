import sys
input = sys.stdin.readline

n = int(input())

f = [1,1,1] # f(1), f(2), f(3) 선언
cnt = 2

while n > len(f):  # 만약 f(n)까지 아직 구해지지 않았다면
    f.append(f[cnt-2]+f[cnt])  # f[cnt-2]+f[cnt]를 추가
    cnt += 1

print(f[n-1])  # 답 출력