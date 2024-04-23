import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

name =[]
score = []
for i in range(n):
    na, s = input().split()
    name.append(na)
    s = int(s)
    score.append(s)

num = 0

for i in range(k):
    bs = input()
    bs = bs.strip()
    index = name.index(bs)
    num += score[index]
    del name[index]
    del score[index]

score.sort(reverse=True)
maxnum = num
minnum = num
for i in range(m-k):
    maxnum += score[i]
    minnum += score[-(i+1)]
    
print(minnum, maxnum)