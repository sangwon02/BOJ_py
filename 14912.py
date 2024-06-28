import sys
input = sys.stdin.readline

n, m = map(int, input().split())
m = str(m)
li = []
for i in range(1, 1+n):  # 1부터 n까지의 정수들을
    s = str(i)  # 리스트에 문자열로 저장
    li.append(s)
cnt = 0

for i in li:  # 리스트에 있는 문자열을 하나씩 꺼내서
    for j in i:  # 꺼낸 문자열의 문자를 하나씩 체크하면서
        if j == m:  # m과 같다면
            cnt += 1  # cnt에 +1

print(cnt)  # 답 출력