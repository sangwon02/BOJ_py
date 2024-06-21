import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = []
li = list(map(int, input().split()))  # 리스트 입력 받고
li.sort(reverse=False)  # 오름차순으로 정렬
print(li[k-1])  # k번쨰 숫자 출력