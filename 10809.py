st = input() #문자열을 입력 받음
alpha = list(range(97,123)) #리스트에 a부터 z까지의 아스키 코드 추가 

for x in alpha : #x가 alpha(리스트)의 문자를 대입하며 반복
    print(st.find(chr(x))) #문자가 각 아스키코드에 대응하는 문자가 몇개 있는지 출력
