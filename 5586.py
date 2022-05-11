str1 = input() #문자를 입력받음
cnt1 = 0 #JOI횟수 셀 변수
cnt2 = 0 #IOI횟수 셀 변수
for i in range(len(str1)-2): #문자릐 길이보다 2작은 수만큼 반복
    if str1[i:i+3] == "JOI": #i번째 문자부터 i+3문자가 JOI면
        cnt1 += 1 #cnt1 +1
    elif str1[i:i+3] == "IOI": #i번째 문자부터 i+3문자가 IOI면
        cnt2 += 1 #cnt2 +1
print(cnt1) #cnt1 출력
print(cnt2) #cnt2 출력