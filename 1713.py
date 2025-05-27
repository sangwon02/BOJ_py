from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
count = int(input())
student = list(map(int, input().split()))
picture = []
exist = False
test = 0

for s in student:
    test += 1
    if (len(picture) < n):
        exist = False
        for i in range(len(picture)):
            if s == picture[i][0]:
                picture[i][1] += 1
                exist = True
                break
        if (exist == False):
            picture.append([s, 1])
    else:
        exist = False
        for i in range(len(picture)):
            if s == picture[i][0]:
                picture[i][1] += 1
                exist = True
                break
        if (exist == False):
            minscore = 1001
            for i in range(n):
                minscore = min(picture[i][1], minscore)
            for i in range(n):
                if (picture[i][1] == minscore):
                    del picture[i]
                    break

            picture.append([s, 1])
        
picture.sort(key=lambda x:x[0])
for p in picture:
    print(p[0], end=" ")