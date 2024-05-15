import sys
input = sys.stdin.readline

n = int(input())
grade = []

for i in range(n):
    li = []
    li = input().split()  # 학생의 이름과 성적을 받아 저장
    grade.append(li)
    
# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 정렬
grade.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 학생 이름 출력
for i in range(n):
    print(grade[i][0])