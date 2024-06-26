import sys
input = sys.stdin.readline

n, m = map(int, input().split())

setA = set(map(int, input().split()))  # A의 원소들을 입력 받음
setB = set(map(int, input().split()))  # B의 원소들을 입력 받음

result = list(setA-setB)  # A에는 속하면서 B에는 속하지 않는 원소를 리스트에 넣어줌
result.sort(reverse=False)  # 오름차순으로 정렬

print(len(result))  # 원소의 개수 출력
if len(result) > 0:  # 만약 원소의 개수가 1개 이상이라면
    print(" ".join(map(str, result)))  # 원소들 출력