import sys
input = sys.stdin.readline

n = int(input())  # N 입력 받은
a = list(map(int, input().split()))  # A에 있는 수 입력 받음
b = list(map(int, input().split()))  # B에 있는 수 입력 받음

a.sort(reverse=False)  # A에 있는 숫자 오름차순으로 정렬
b.sort(reverse=True)  # A에 있는 숫자 오름차순으로 정렬
s = 0  
for i in range(n):  # 각 리스트에 있는 숫자끼리 곱하고 더한 값을 출력
    s += a[i]*b[i]
    
print(s)