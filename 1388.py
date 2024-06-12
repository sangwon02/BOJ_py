import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = []  # 바닥 타일 저장할 리스트
for _ in range(n):
    li.append(list(input()))

cnt = 0
for i in range(n): # -의 개수 계산
    a = ''
    for j in range(m):
        if li[i][j] == '-':  # 검사하는 부분이 -이고
            if li[i][j] != a:  # 전의 바닥 장식과 다르다면
                cnt += 1  # +1
        a = li[i][j]

for j in range(m): # ㅣ의 개수 계산
    a = ''
    for i in range(n):
        if li[i][j] == '|':  # 검사하는 부분이 |이고
            if li[i][j] != a:  # 전의 바닥 장식과 다르다면
                cnt += 1  # +1
        a = li[i][j]

print(cnt)
