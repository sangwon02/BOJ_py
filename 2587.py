import sys
input = sys.stdin.readline

li = []  # 정수를 담을 리스트 생성

for _ in range(5):  # 5개 입력받아 리스트에 저장
    li.append(int(input()))
    
li.sort(reverse = False)  # 오름차순으로 정렬

print(sum(li)//5)  # 평균값 출력
print(li[2])  # 중앙값 출력
