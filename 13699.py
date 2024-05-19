import sys
input = sys.stdin.readline

n = int(input())
t = [1]  # t(0) = 1을 생성

for i in range(n):  # 주어진 수열 t(n을 생성)
    num = 0
    for j in range(len(t)):
        num += t[j]*t[-(j+1)]  
        # t(len(t))=t(0)*t(len(t)-1)+t(1)*t(len(t)-2)+...+t(len(t)-1)*t(0) 한 후
    t.append(num)  # t에 저장

print(t[n])  # 답 출력