N = int(input())
li = list(map(int, input().split()))
scale = int(input())
sum1 = 0

for i in range(N):
    if li[i]==0:
        continue
    n1 = li[i]//scale
    if li[i]%scale:
        n1 += 1
    sum1 += scale*n1
    
print(sum1)