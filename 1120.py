import sys
input = sys.stdin.readline

# 초기 답안(정답)
a, b = map(str, input().split())

differ = len(b)-len(a)
min1 = 50
if differ > 0:
    for i in range(differ+1):
        min2 = 0
        for j in range(len(a)):
            if a[j] != b[j+i]:
                min2 += 1
        if min1 > min2:
            min1 = min2
    print(min1)
else:
    min2 = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            min2 += 1
    print(min2)

# 우수 답안

a, b = map(str, input().split())

answer = []
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    answer.append(count)

print(min(answer))