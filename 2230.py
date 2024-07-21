import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
    
a.sort(reverse=False)  # 오름차순으로 정렬 
result = 10**10

pointer1 = 0
pointer2 = 0

while pointer1<n and pointer2<n: # 포인터 값이 리스트의 길이보다 작아야함
    if (a[pointer2] - a[pointer1]) < m:  # m보다 작을 경우 pointer2을 늘려주어 탐색
        pointer2 += 1
    else:  # m보다 크다면
        result = min(result, a[pointer2]-a[pointer1])  # result값과 비교해서 작은 값을 저장
        pointer1 += 1


print(result)