str1 = input() #문자를 입력받음
str2 = ""  #아무것도 없은 문자열
#CAMBRIDGE에 포함된 알파벳을 넣은 리스트
str_list = ["C", "A", "M", "B", "R", "I", "D", "G", "E"] 


for i in str1: #str1에 있는 문자수만큼 반복
    if i not in str_list: #만약 i가 리스트안에 있다면
        str2 += i #i를 str2에 추가함

print(str2) #str2를 출력한다.