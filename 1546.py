n = int(input()) #입력 받을 값의 수
list1 = list(map(int, input().split()))#공백을 기준으로 정수를 리스트에 입력 받음
list2 = [] #리스트 생성
num = 0 
mscore = max(list1) #가장 높은 점수 저장
for i in list1: #리스트1을 i에 하나씩 저장하면서 반복
    list2.append((i/mscore)*100) #새로운 점수를 리스트2에 저장

print(sum(list2)/n) #새로운 평균 출력