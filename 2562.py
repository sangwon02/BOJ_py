num = [] #숫자를 저장할 리스트

for i in range(9): #9번 반복
    a = int(input()) #숫자를 입력 받음
    num.append(a) #입력받은 숫자를 리스트에 저장함
a = num[0] #첫번째 리스트의 값을 a에 저장
for n in num: #리스트에 있는 요소의 수만큼 반복(n에 그 순서의 리스트값 할당)
    if n >= a: #만약 n이 a보다 크다면
        a = n #a에 n을 저장
b = int(num.index(a)) #b에 a의 인덱스값을 찾아 저장 
print(a, b+1) #a와 b+1을 출력