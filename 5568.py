from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
li = []
for i in range(n):  # 카드들을 전부 입력 받음
    li.append(input().strip())
result = []

for i in permutations(li, k):  # permutarions함수를 이용해 조합을 만들고
    s = ''.join(i)  # 튜플형을 문자열로 바꾸어준다.
    if s not in result:  # 만약 문자열이 result리스트에 없다면
        result.append(s)  # result에 추가
print(len(result))  # result 원소의 개수 출력
