import sys
input = sys.stdin.readline

n = int(input())  # 참가자 수 입력 받고

max_participant = 0  # 가장 높은 점수를 가진 참가자를 넣을 변수
max_score = 0  # 가장 높은 점수를 넣을 변수

for i in range(n):  
    li = []
    li = list(map(int, input().split()))

    if (li[0]+li[1]+li[2])%10 >= max_score:
        max_participant = i+1
        max_score = (li[0]+li[1]+li[2])%10
        if max_score == 9:
            continue

    if (li[0]+li[1]+li[3])%10 >= max_score:
        max_participant = i+1
        max_score = (li[0]+li[1]+li[3])%10
        if max_score == 9:
            continue

    if (li[0]+li[1]+li[4])%10 >= max_score:
        max_participant = i+1
        max_score = (li[0]+li[1]+li[4])%10
        if max_score == 9:
            continue

    if (li[0]+li[2]+li[3])%10 >= max_score:
        max_participant = i+1
        max_score = (li[0]+li[2]+li[3])%10
        if max_score == 9:
            continue

    if (li[0]+li[2]+li[4])%10 >= max_score:
        max_participant = i+1
        max_score = (li[0]+li[2]+li[4])%10
        if max_score == 9:
            continue

    if (li[0]+li[3]+li[4])%10 >= max_score:
        max_participant = i+1
        max_score = (li[0]+li[3]+li[4])%10    
        if max_score == 9:
            continue

    if (li[1]+li[2]+li[3])%10 >= max_score:
        max_participant = i+1
        max_score = (li[1]+li[2]+li[3])%10
        if max_score == 9:
            continue

    if (li[1]+li[2]+li[4])%10 >= max_score:
        max_participant = i+1
        max_score = (li[1]+li[2]+li[4])%10
        if max_score == 9:
            continue

    if (li[1]+li[3]+li[4])%10 >= max_score:
        max_participant = i+1
        max_score = (li[1]+li[3]+li[4])%10
        if max_score == 9:
            continue

    if (li[2]+li[3]+li[4])%10 >= max_score:
        max_participant = i+1
        max_score = (li[2]+li[3]+li[4])%10
        if max_score == 9:
            continue

    
print(max_participant)

# 나중에 짠 코드

from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())  # 참가자 수 입력 받고

max_participant = 0  # 가장 높은 점수를 가진 참가자를 넣을 변수
max_score = 0  # 가장 높은 점수를 넣을 변수
li = []  # 점수들을 저장할 리스트 생성

for i in range(n):
    li1 = list(map(int, input().split()))  # 카드들을 입력 받고
    li.append(li1)  # 리스트에 저장


for i in range(n):  # 가장 높은 점수를 가진 참가자 찾기
    # 파이썬 내장 함수인 combinations를 사용해 combi에 조합 값들을 저장
    combi = list(combinations(li[i], 3))  
    score = 0
    for j in combi:  # 참가자들 별로 각 조합 값들을 꺼내서
        score = max(score, sum(j) % 10)  # 조합 값의 일의 자리수중 가장 큰 수가 참가자의 점수
    if score >= max_score:  # 만약 참가자의 점수가 그 전에 있던 가장 큰 점수보다 크다면
        max_participant = i + 1  # 새로운 참가자와 점수로 갱신
        max_score = score

print(max_participant)  # 가장 점수가 높은 참가자 출력