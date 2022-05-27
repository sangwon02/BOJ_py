st = input().upper() #문자열을 입력 받음(대문자로)
st1 = list(set(st)) #리스트에 문자열의 문자를 집어넣음

li = []
for x in st1 : #리스트를 x에 대입하면서 반복
    cnt = st.count(x) #x가 문자에 몇개 들어있는지 찾아서
    li.append(cnt) #li(리스트에 저장)

if li.count(max(li)) > 1 :  #가장 많이 사용된 문자가 여러개이면
    print('?') #? 출력
else : #아니면
    #가장 많이 사용된 문자를 프린트
    max_index = li.index(max(li)) 
    print(st1[max_index])