n = int(input()) #반복할 숫자 받음

for i in range(n): #n만큼 반복
    a = input() #문자 입력 받음
    score = 0 #점수
    sum = 0 #점수의 합
    for j in a: #a의 문자를 j에 대입하면서 반복
        if j == 'O': #O면
            score += 1 #score에 +1
        else: #O이 아니면
            score = 0 #다시 score초기화
        sum += score #점수의 합
    print(sum)#점수의 합 출력