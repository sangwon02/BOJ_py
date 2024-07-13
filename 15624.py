import sys
input = sys.stdin.readline

n = int(input())

f = [0,1] # f(1), f(2) 선언
cnt = 1

while n >= len(f):  # 만약 f(n)까지 아직 구해지지 않았다면
    f.append((f[cnt-1]+f[cnt]) % 1000000007)  # f[cnt-1]+f[cnt]를 추가
    cnt += 1

print(f[n])  # 답 출력