import re

n = int(input()) # 정수를 입력 받음
sum=0 
str1 = input() #문자열을 입력 받음

li = re.findall("\d+", str1) #하나 혹은 그 이상 연결된 숫자를 찾음



for i in li: ##i에 li의 값을 대입하면서 반복
    sum += int(i) #i를 sum에 더함
print(sum) #sum출력

# \d는 숫자를 한 글자만 찾는다.
# +는 '하나 혹은 그 이상 연결된' 이란 뜻이다.
# 즉, \d+는 '하나 혹은 그 이상 연결된 숫자`이다.
