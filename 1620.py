import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name = {}  # value에 포켓몬의 이름을 담을 딕셔너리
num = {}  # key에 포켓몬의 이름을 담을 딕셔너리
for i in range(1, n+1):
    s = input().strip()
    name[i] = s
    num[s] = i

for i in range(m):
    s = input().strip()
    if s[0].isalpha():  # 만약 s가 알파벳이라면
        print(num[s])
    else:
        print(name[int(s)])  # 만약 s가 숫자라면