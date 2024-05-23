import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = []
num = []
for i in range(1,n+1):
    num.append(i)
cnt1 = -1
cnt2 = 1

while len(num)!=0:
    if cnt1 >= len(num)-1:
        cnt1 = -1
    cnt1 += 1
    if cnt2%k == 0:
        cnt2 = 0
        m = num[cnt1]
        del num[cnt1]
        result.append(m)
        cnt1 -= 1
    cnt2 += 1

print("<",end="")
for i in range(n-1):
    print(result[i],end=", ")
print(result[n-1], end = "")
print(">",end="")
