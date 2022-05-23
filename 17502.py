n = int(input()) #정수(문자열의 수)를 입력 받음
str1 = input() #문자열을 입력 받음
str_list = list(str1) #리스트에 문자열의 문자를 입력 받음

for i in range(n): #n만큼 반복
    if str_list[i] == "?" and str_list[-(i+1)] == "?": #만약 i번째 원소와 -(i+1)번째 원소가 ?면
        str_list[i] = "a" #둘다 a로 바꿔줌
        str_list[-(i+1)] = "a"
    elif str_list[i] == "?": #i번째 원소가 ?면
        str_list[i] =str_list[-(i+1)] #-(i+1)번째 원소랑 같게 만듬

print("".join(str_list)) #원소를 문자열의 형태로 출력