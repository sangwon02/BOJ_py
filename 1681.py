n1, n2 = map(int, input().split()) #원하지 않는 숫자 n2, 학생수 n1

n2 = str(n2) #n2를 문자로 바꾸어줌

n3 = 0
n4 = 0

while n1 != n3: #n1이 n3와 같을때 까지 반복
    n4 += 1 #n4를 하나식 증가시켜줌
    if n2 in str(n4): #n4안에 n2가 들어있으면 n3를 +1 해주지 않고 다시 반복
        continue 
    n3 += 1 #n4안에 n2가 들어있지 않으면 n3를 +1 해줌

print(n4) #마지막 숫자 출력