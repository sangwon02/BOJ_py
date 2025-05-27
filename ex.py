i = 0
li = []
# 이게 더 빠름 이거 쓰는 습관 들이기
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()  # 문자열 받을때
n, m = map(int, input().split())

#리스트 요소 하나하나 띄어쓰기 출력
print(" ".join(map(str, li)))

from itertools import combinations

map = [list(map(int, input().split())) for _ in range(n)]

n = int(input())

str1 = input()

n1, n2 = map(int, input().split())

print(i, end ="")

print(*li)  # 리스트 뛰어쓰기하며 출력

li.append(int(input())) #for문으로 입력 받을때

# 주의 sys.stdin.readline 쓰면 안됨
li.append(list(map(int, input()))) # 띄어쓰기 없이 입력 받아도 정수 하나씩 저장

li = list(map(int, input().split()))

set1 = set(map(int, input().split())) # 집합 중복된 값 제거하고 리스트보다 빠름

li = input().split() # 문자열 띄어쓰기 별로 나누어서 저장

print("dfsfsdfsdfsdf"[:3])
#3번째 까지 문자열 출력

li.sort(reverse=False)
#숫자, 문자 오름차순으로 정렬
li.sort(reverse=True)
#숫자, 문자 내림차순으로 정렬

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
    
print(*li) # 리스트 대괄호 없이 출력

array = list(range(1,n+1)) # 1부터 n까지의 리스트 생성

li.append(k)
#리스트에 항목추가
for i in range(n):
    li.append(int(input()))

li = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
st = set(li) #집합set으로 변환
li = list(st) #list로 변환

arr = [[0] * 100 for _ in range(100)] # 배열 만들기



import sys

def dfs(position, distance):
    global min_distance
    if position > D:  # 목표 도착 지점을 초과한 경우
        return
    if position == D:  # 정확히 도착한 경우 최솟값 갱신
        min_distance = min(min_distance, distance)
        return

    # 현재 위치에서 한 칸씩 이동하는 기본 경로
    dfs(position + 1, distance + 1)

    # 모든 지름길을 확인하며 사용할 수 있으면 이동
    for start, end, shortcut in shortcuts:
        if position == start:
            dfs(end, distance + shortcut)

# 입력 처리
N, D = map(int, sys.stdin.readline().split())
shortcuts = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 최소 거리 초기화
min_distance = D  # 최악의 경우, 그냥 1씩 이동하는 거리

dfs(0, 0)
print(min_distance)
