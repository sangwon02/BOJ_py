while True: #무한 반복
    cnt = [0] * 26 #알파벳 개수만큼 리스트 생성
    s = input() #문자를 입력받음
    if s == "*": #s가 *이면
        exit() #종료
    else: #*이 아니면
        for i in range(len(s)): #문자열의 길이만큼 반복
            if ord(s[i])!=32 : #공백이 아니라면
                cnt[ord(s[i]) - 97]=1 #리스트 알파벳의 자리에 1해줌
        if sum(cnt) == 26: #모든 리스트의 합이 26이면
            print("Y") #Y프린트
        else:  #아니면
            print("N") #N을 프린트
        
