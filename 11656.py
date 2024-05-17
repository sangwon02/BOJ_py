import sys
input = sys.stdin.readline

s = input().strip()  # 문자열을 입력 받고
li = []
for i in range(len(s)):  # 문자열의 접미사들을 리스트에 저장
    li.append(s[i:])

li.sort(reverse=False)  # 사전순으로 정렬 후

for i in li:  # 답 출력
    print(i)