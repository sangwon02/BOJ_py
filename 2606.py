import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
couple = []
for i in range(m):
    n1, n2 = map(int, input().split())
    couple.append([n1, n2])
couple.sort(reverse=False)
result = {1}
for i in couple:
    if (i[0] in result) or (i[1] in result):
        result.add(i[0])
        result.add(i[1])
print(len(result)-1)