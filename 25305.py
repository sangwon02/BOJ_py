import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 학생 수와 상을 받는 학생 수 입력 받음

num = list(map(int, input().split()))  # 리스트에 각 학생의 점수 입력 받고

num.sort(reverse=True)  # 리스트 내림차순 정렬

print(num[k-1])  # 커트라인의 점수를 출력