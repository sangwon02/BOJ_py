a = int(input()) #3개의 숫자를 각각 a, b, c에 입력받음
b = int(input())
c = int(input())
x = a*b*c #a, b, c를 곱한 값을 x에 저장
n1 = 10 
n3 = 1 
list = [0,0,0,0,0,0,0,0,0,0,0]

while True: #무한 반복
    n2 = (x%n1)//n3 #n2에 (x%n1)//n3를 저장해준다.
    #1번째 시도하면 마지막 첫째자리의 숫자
    #2번째 시도하면 마지막 둘째자리의 숫자
    #3번째 시도하면 마지막 셋째자리의 숫자
    #.....
    list[n2]=list[n2]+1 #n2가 있는 위치에 +1
    n1 = n1*10 #각각의 자리수의 숫자를 찾기위해 10씩 곱해준다.
    n3 = n3*10
    if n3>x: #만약 n3의 값이 x보다 작으면 
        break #while문 종료
for i in range(10): #각 리스트의 값을 출력
    print(list[i])