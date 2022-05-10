n = int(input()) #전투 횟수 입력받음

for i in range(n): #n만큼 반복
    #공백을 구분하여 정수 입력받음
    li1 = list(map(int, input().split())) 
    li2 = list(map(int, input().split()))
    #각각의 종족의 따라 점수를 구해 더해준다
    sum1 = li1[0] + li1[1]*2 + li1[2]*3 + li1[3]*3 + li1[4]*4 + li1[5]*10 
    sum2 = li2[0] + li2[1]*2 + li2[2]*2 + li2[3]*2 + li2[4]*3 + li2[5]*5 + li2[6]*10
    #각 전투에 대해 전투 번호를 함께 출력한다 
    if sum1 > sum2:#간달프의 군대가 이기면
        print("Battle %d: Good triumphs over Evil"%(i+1)) #간달프의 군대가 이겼다고 출력
    elif sum1 < sum2: #사우론의 군대가 이기면
        print("Battle %d: Evil eradicates all trace of Good"%(i+1)) #사우론의 군대가 이겼다고 출력
    else: #비기면
        print("Battle %d: No victor on this battle field"%(i+1))  #비겼다고 출력