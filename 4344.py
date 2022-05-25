n = int(input()) #테스트 케이스의 개수를 입력 받음
num = 0 

for i in range(n): #n만큼 반복
    list1 = list(map(int, input().split())) #공백을 구분해 정수를 입력 받아 리스트에 저장
    num = sum(list1[1:])/list1[0] #사람의 수(첫번째 수)와 점수의 합을 나누어주어 평균을 구한다.
    st = 0
    for j in list1[1:]:#점수들을 j에 대입하면서 반복
        if j > num: #j가 num보다 크면
            st+=1 #st +1
    rate = st/list1[0] *100 #평균을 넘는 사람의 비중을 저장
    print(f'{rate:.3f}%')#rate를 소수점 셋째 자리까지 출력
