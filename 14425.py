import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = set() # 집합 s 선언
res = 0 # 답을 담을 변수

for _ in range(n):
    s.add(input())  # 문자열을 입력 받고 집합 s에 넣어줌
    
for _ in range(m):
    st = input()  # 문자열을 입력 받고
    if st in s:  # 만약 집합 s에 있다면 
        res += 1  # res의 값 +1
print(res)  # res(답) 출력