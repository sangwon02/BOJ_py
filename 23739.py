n = int(input())
sum1 = 0
cnt = 0
li = []

for i in range(n):
    li.append(int(input()))

    if (li[i])/2<=30-sum1:
        cnt = cnt + 1
    sum1 = li[i] + sum1 
    if sum1 >= 30:
        sum1 = 0
print(cnt)