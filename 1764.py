#처음에는 집합 대신에 리스트를 사용했는데 시간초과가 떠서
#집합으로 바꾸어서 사용하였다.
N, M = map(int, input().split())
set1 = set()
set2 = set()

for i in range(N):
    set1.add(input())

for i in range(M):
    set2.add(input())

li = sorted(list(set1 & set2))

print(len(li))
for i in li:
    print(i)