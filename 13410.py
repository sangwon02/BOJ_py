n1, n2 = map(int, input().split()) #정수 두개를 입력 받음
li = [] #리스트 선언

for i in range(n2): #n2만큼 반복
    a = n1*(i+1) 
    li.append(int(str(a)[::-1])) #a를 반대로 바꿔 리스트에 넣음 

print(max(li)) #리스트에서 가장 큰값을 프린트