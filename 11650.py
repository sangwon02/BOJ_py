#시간 초과 ㅠㅠ
""" 

import sys

n = int(sys.stdin.readline())
li1 = []
li2 = []

for i in range(n):
    n1, n2 = map(int, sys.stdin.readline().split())
    li1.append(n1)
    li2.append(n2)

for j in range(len(li1)):
    k = len(li1) - j
    for i in range(1, k):
        if li1[i-1] > li1[i]:
            temp = li1[i-1]
            li1[i-1] = li1[i]
            li1[i] = temp
            temp = li2[i-1]
            li2[i-1] = li2[i]
            li2[i] = temp
        if li1[i-1] == li1[i]:
            if li2[i-1] > li2[i]:
                temp = li2[i-1]
                li2[i-1] = li2[i]
                li2[i] = temp

for i in range(n):
    print(li1[i], li2[i])
"""

import sys

n = int(sys.stdin.readline())

li = []

for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort(key=lambda x: (x[0], x[1]))

for i in li:
    print(i[0], i[1])