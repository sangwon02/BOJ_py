L = int(input())
li = [0] * (L + 1)
N = int(input())
num1 = [0] * (N + 1)
maxnum, M_cnt = 0, 0

for i in range(1, N + 1):
    P, K = map(int, input().split())
    if K - P - 1 > M_cnt:
        maxnum = i
        M_cnt = K-P-1
    cnt = 0
    for j in range(P, K + 1):
        if not li[j]:
            li[j] = 1
            cnt += 1
    num1[i] = cnt

print(maxnum)
print(num1.index(max(num1)))