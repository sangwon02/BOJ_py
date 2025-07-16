import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = []
for _ in range(n):
    li.append(int(input()))
    
li.sort(reverse=False)  # 오름차순으로 정렬 
result = 10**10

n1 = 0
n2 = 0

while result != m: # 결과 값이 m과 같아지면 종료
    if result > (li[n2] - li[n1]) and li[n2] - li[n1] >= m:
        result = li[n2] - li[n1]
    if li[n2] - li[n1] < m:
        if n2 != (n-1):
            n2 += 1
        elif n2 == (n-1):  # 마지막 인덱스에 도달하면
            break # 반복문 종료
    else:
        n1 += 1
    
print(result)  # 결과 출력