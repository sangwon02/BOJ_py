import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):  # 물건들의 가격을 저장한다.
    li.append(int(input()))
li.sort(reverse=True)  # 내림차순으로 정렬
result = 0
for i in range(2, len(li), 3):  # 3의 배수의 위치에 있는 수들을 더한 값을 
    result += li[i]
print(sum(li)-result)  # 빼준 값을 출력