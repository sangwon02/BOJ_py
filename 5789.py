N = int(input()) #반복할 수를 입력 받음

for i in range(N): #N만큼 반복
    s = input() #문자열을 입력받음
    if s[len(s)//2] == s[len(s)//2 -1]: #중심부분의 문자가 같으면
        print("Do-it") #Do-it 출력
    else: #다르면
        print("Do-it-Not")#Do-it-Not출력