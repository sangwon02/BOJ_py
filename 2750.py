n = int(input()) #입력 받을 숫자의 개수를 입력 받음
li = [] #리스트 생성
 
for i in range(n): #n만큼 반복
    li.append(int(input())) #정수를 입력 받아 리스트에 넣어줌

li.sort(reverse=False) #리스트를 오름차순으로 정렬

#리스트 출력
for i in li: 
    print(i)