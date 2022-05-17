st = input() #문자열을 입력 받음
alpha = list(range(97,123)) #리스트에 a부터 z까지의 아스키 코드 추가 

for x in alpha : #x가 alpha(리스트)의 문자를 대입하며 반복
    print(st.find(chr(x)), end=" ") #x가 단어에 포함되어 있지 않다면 -1을 출력
    #a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력
