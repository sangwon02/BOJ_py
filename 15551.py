n1, n2 = map(int, input().split())
A = list(map(int, input().split(",")))
cnt = 1

for k in range(n2):
    for i in range(n1-cnt):
        a = A[i]
        A[i]=A[i+1]-a
    cnt += 1

for j in range(n1-n2):
    print(A[j], end="")
    if j<n1-n2-1:
        print(",",end="")