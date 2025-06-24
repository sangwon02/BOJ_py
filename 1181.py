import sys
input = sys.stdin.readline

n = int(input())
set_data = set()  # 세트 선언 (중복되 문자열은 저장 안하기 위해)

for _ in range(n):  # 문자열 입력 받고
    set_data.add(input().strip())

list_data = list(set_data)  # 세트에 있는 요소를 리스트로 저장해주고 
list_data.sort(reverse=False)  # 먼저 오름차순으로 정렬
list_data.sort(key=len)   # 이후 길이순으로 정렬

for i in list_data:  # 답 출력
    print(i)
