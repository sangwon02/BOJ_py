a, b, v= map(int, input().split()) #공백을 구분하여 정수를 3개 입력 받음
k = (v-b)/(a-b) #남은 거리와 하루에 올라는 거리를 나누어주어 저장함 

if k == int(k): #k가 정수면
    print(int(k)) #k만 프린트
else: #정수가 아니면
    print(int(k)+1) #k를 반올림 해주어 정수로 출력
 