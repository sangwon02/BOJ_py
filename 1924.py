Day = 0 
li1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
li2 = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
n1, n2 = map(int,input().split()) #월일을 입력받음
 
for i in range(n1-1): #n1-1만큼 반복
    Day = Day + li1[i] #월에 따른 날짜를 더해준다
Day = (Day + n2) % 7 #남은 날짜를 더해주고 7로 나눈 나머지를 저장
 
print(li2[Day]) #무슨 요일인지 출력 