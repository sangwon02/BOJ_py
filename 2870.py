import sys
import re  # re함수 불러옴
input = sys.stdin.readline

n = int(input())
result = []

for i in range(n):
    s = input().strip()
    # re함수를 사용해 숫자들을 발췌한 수들을 numbers에 저장
    numbers = re.findall(r'\d+', s)  
    for j in numbers: 
        result.append(int(j))  # 정수형으로 변환 후 result에 저장

result.sort()  # 비내림차순으로 정렬

for i in result:  # 답 출력
    print(i)