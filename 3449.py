n = int(input()) #테스트 케이스의 개수 n

for i in range(n): #n만큼 반복
    str1 = input() #첫번째 숫자 입력 받음
    str2 = input() #두번째 숫자 입력 받음
    cnt = 0 #다른 개수 새주는 변수
    for j in range(len(str1)):#숫자의 자릿수만큼 반복
        if str1[j] != str2[j]: #만약 같은 위치의 숫자가 다르면
            cnt += 1 #cnt += 1
    print("Hamming distance is %d."%cnt)#해밍 거리 출력