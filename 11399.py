import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))  # 사람들 돈 뽑는 시간 받음

li.sort(reverse=False)  # 오름차순으로 정렬
res = 0

for i in range(n):
    res += sum(li[:i+1]) # 첫번째 수부터 i+1수를 더한 수를 res에 저장 

print(res)