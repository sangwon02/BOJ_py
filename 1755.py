import sys
input = sys.stdin.readline

m, n = map(int, input().split())  # 원하는 범위 입력 받음
# 숫자와 알파벳이 매치된 딕셔너리
number_dic_en = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 0: "zero"}
dic = {}  # 각 정수들을 숫자 단위로 나눠 영어로 바꾼 것을 담은 딕셔너리
for i in range(m, n+1):  # i는 m부터 n까지 반복
    s = str
    if i >= 10:  # 만약 i가 10을 넘으면 십의 자리와 일의 자리를 나누어 저장
        s = number_dic_en[i//10] + " " + number_dic_en[i%10]
    else:  # 10을 안넘으면 그냥 저장
        s = number_dic_en[i]
    dic[s] = i  # 딕셔너리에 넣어줌
dic = sorted(dic.items())  # 사전순으로 정렬

for i in range(len(dic)):  # 정답 출력
    if i%10 == 0 and i != 0:  # 정수 열개 출력하면 다음 줄로 넘어감
        print("")
    print(dic[i][1],end=" ")  # 줄 바꿈 없이 출력
print("")