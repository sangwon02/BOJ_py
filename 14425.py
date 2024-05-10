import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nset = set()

for i in range(n):  # n개의 문자열을 집합에 저장 
    nset.add(input().strip())
    
cnt = 0
for i in range(m): 
    s = input().strip()  # 문자열을 입력 받고
    if s in nset:  # 만약 집합에 있는 문자열이라면 
        cnt += 1  # +1 카운트 해줌

print(cnt)  # 답 출력