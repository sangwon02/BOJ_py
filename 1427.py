import sys
input = sys.stdin.readline

n = input()  # 정수 n을 문자열로 입력 받고
li = []
for i in n:  # 각 자리수의 숫자를 문자형으로 리스트에 넣어준다.
    li.append(i)
    
li.sort(reverse = True) # 내림차순으로 정렬해주고

for i in li:  # 리스트안에 있는 요소들을 출력
    print(i, end="")