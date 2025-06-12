import sys
input = sys.stdin.readline

n = int(input())
nli = list(map(int, input().split()))  # 상근이가 가진 카드 입력 받고
m = int(input())
mli = list(map(int, input().split()))  # 비교할 카드 입력 받는다.
# 일단 다 입력 받고

result = {} 
# 정답을 받을 딕셔너리 생성
# 이유) 딕셔너리가 연산이 더 빠르다

for i in range(n):
    result[nli[i]] = 0  
    # nli에 있는 요소들을 result에 추가
    # 매핑은 0으로

for i in mli:  # mli에 있는 정수들을 하나씩 꺼내며 돌고
    if i in result:  # 만약 그게 reslut에 있다면
        print(1, end=" ") # 1을 출력
    else:  # 없으면
        print(0, end=" ") # 0을 출력
