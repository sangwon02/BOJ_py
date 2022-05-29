n = int(input()) #정수를 입력 받음

for i in range(n): #n만큼 반복
    num = [] #리스트 생성
    a = int(input()) #정수를 입력 받음
    b = int(input()) #정수를 입력 받음
    num = [j for j in range(1, b+1)] #리스트에 a부터 b까지 추가
    
    for l in range(a): #a만큼 반복
        for j2 in range(1, b): #1부터 b까지 j2에 대입하면서 반복
            num[j2] += num[j2-1] #j2에 있던 원소에 j2-1를 더함
    print(num[b-1]) #b-1자리에 있는 원소 프린트