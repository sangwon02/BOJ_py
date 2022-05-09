num = [] #입력받은 숫자를 넣어줄 리스트
num1 = [] #42로 나눈 나머지 값을 넣을 리스트
for n in range(10): #10번 반복
    a = int(input()) #숫자를 입력 받음
    num.append(a) #num에 추가
    num[n] = num[n]%42 #넣은 숫자를 42로 나눈 나머지로 변경

for v in num:#num 원소의 개수만큼 반복
    if v not in num1: #num1안에 v가 없으면
        num1.append(v) #num1에 v추가

print(len(num1)) #num1 원소의 개수 프린트 
    
