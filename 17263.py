n = int(input()) #문자를 넣을 정수 입력 받음

li = list(map(int, input().split())) #공백을 구분하여 정수를 리스트에 입력 받음

li.sort(reverse=False) #리스트르 오름차순으로 정렬한다

print(li[n-1]) #리스트의 마지막 원소 출력