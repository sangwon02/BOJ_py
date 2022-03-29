L = int(input())
N = int(input())
maxnum = 0
num = 0
num1 = 0
num2 = 0
li = []

for i in range(L):
    li.append(0)
for i in range(N):
    n1, n2 = map(int, input().split())
    for j in range(n1, n2+1, 1):
        if li[j] == 0:
            li[j] = i + 1
    if n2 - n1 > maxnum:
        maxnum = n2 - n1
        num = i + 1

remove_set = {0}
li = [i for i in li if i not in remove_set]

print(num)
print(max(li))