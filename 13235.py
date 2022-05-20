str1 = input() #문자열을 입력 받음
str_list = list(str1) #문자열의 문자들을 리스트에 넣는다
check = "true" 

for i in range(len(str1)//2 + 1): #(문자열의 길이의 반 + 1)만큼 반복
    if str_list[i] != str_list[-(i+1)]: #만약 i번째 문자와 뒤에서 -(i+1)번때 문자가 다르면
        check = "false" #check는 false

print(check) #check 프린트