num = int(input()) #숫자를 입력 받음

for i in range(1, num+1):  
    num1 = sum((map(int, str(i)))) #i의 각자리수의 합을 num1에 저장
    su = i + num1 #i와 num1의 합을 su에 저장

    if su == num: #만약 su와 num의 값이 같다면 i가 num의 생성자
        print(i) #i 출력
        break #for문 멈춤
    if i == num: #입력받은 숫자까지 탐색했으나 분해합이 없으면
        print(0) #0을 출력함