n = int(input())#입력 받을 숫자의 자리수
n1 = input() #숫자 입력 받음
sum1 = 0 #합을 저장할 변수

for i in n1: #n1의 문자열을 i에 대입하면서 반복
    sum1 += int(i) #sum1에 i를 더함

print(sum1) #출력
