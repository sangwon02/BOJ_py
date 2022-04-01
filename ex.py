i = 0

import sys
n = int(sys.stdin.readline())

n = int(input())

str1 = input()

n1, n2 = map(int, input().split())

print(i, end ="")

li = list(map(int, input().split()))

set1 = set(map(int, input().split()))

li = input().split()

print("dfsfsdfsdfsdf"[:3])
#3번째 까지 문자열 출력

li.sort(reverse=False)
#숫자 오름차순으로 정렬
li.sort(reverse=True)
#숫자 내림차순으로 정렬

del li[0] 
#리스트 첫번째 값 제거

min(li), max(li)
#가장 작은 값과 큰 값 출력

li =[]
k = 0

num = 0
while num <= 100:
    print(num)
    num = num + 1

li.append(k)
#리스트에 항목추가
for i in range(n):
    li.append(int(input()))