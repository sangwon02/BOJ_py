import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

li.sort(reverse=False)  # 오름차순으로 정렬
result = 0

for i in range(n):
    result += sum(li[:i+1]) # 첫번째 수부터 i+1수를 더한 수를 result에 저장 

print(result)